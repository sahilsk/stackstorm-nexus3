import sys
from nexuscli.nexus_client import NexusClient

from st2common.runners.base_action import Action

__all__ = [
    'BaseAction'
]

class BaseAction(Action):

    def __init__(self, config):
        super(BaseAction, self).__init__(config)
