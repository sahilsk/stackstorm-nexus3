import sys
from lib import base
from st2common.runners.base_action import Action
from nexuscli.repository import Repository
from nexuscli.nexus_client import NexusClient
from nexuscli.exception import *


class ActionManager(base.BaseAction):

    def run(self, **kwargs):
        try:
            requested_action = kwargs.pop('action')
        except KeyError as error:
            raise Exception(
                "'action' parameter is not defined. Error: %s " % error)
        config_profile = kwargs.pop('config_profile')

        self.logger.debug(kwargs)
        self.logger.info("config profile: %s " % kwargs.get('config_profile'))
        default_profile = self.config.get('default_profile', None)
        final_profile = config_profile
        if final_profile is None:
            final_profile = default_profile

        if final_profile is None:
            raise Exception(
                "Neither default profile, nor config_profile option is set")

        profiles = self.config.get('profiles')
        profile = profiles.get(final_profile, None)

        if profile is None:
            raise Exception("Config Profile: %s not found" % final_profile)

        nexus_connection = {
            "url": self.config.get('url', None),
            "verify": self.config.get('verify', None),
            "user": self.config.get('user', None),
            "password": self.config.get('password', None)
        }
        nexus_connection.update(profile)

        nexus_client = None
        try:
            self.logger.debug("connection string: %s \n" % nexus_connection)
            nexus_client = NexusClient(**nexus_connection)
        except Exception as error:
            self.logger.error("Couldn't instantiate nexus client %s" % error)
            return (False, error)

        # Fire request
        response =  None,
        success = True
        
        [verb, resource] = requested_action.split('_')
        dialer = getattr(nexus_client, resource)
        if verb == "list":
            if resource == "repositories":
                response = dialer.raw_list()
            else:
                response = dialer.list()
        elif verb == "create":
            payload = kwargs.get('data', '')

            if resource == "repositories":
                repo_type = kwargs.pop('type')
                payload = Repository(repo_type, **kwargs)

            try:
                if resource == "scripts":
                    response = dialer.create_if_missing(payload)
                else:
                    response = dialer.create(payload)
            except NexusClientCreateRepositoryError as error:
                response = "Failed to create %s. Most likely reason, same name resource already exist." % (
                    resource)
                success = False
            except Exception as error:
                response = "Failed to create %s. Error %s" % error
                success = False

        elif verb == "delete":
           response =  dialer.delete(kwargs.pop('name'))
        elif verb == "get":
            if resource == "repositories":
                response = dialer.get_raw_by_name(kwargs.pop('name'))
            else:
                response = dialer.get(kwargs.pop('name'))
        elif verb == "run" and resource == "scripts":
            response = dialer.run(kwargs.pop('name'), kwargs.pop('data'))

        return (success, response)
