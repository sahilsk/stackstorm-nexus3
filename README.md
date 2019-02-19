# Stackstorm-Sontatype Nexus3


Sontatype nexus3 stackstorm pack

## Installation


Install this pack with: `st2 pack install file:///$PWD`

Or if in remote repository: `st2 pack install https://github.com/MY/PACK`

## Configuration

Copy the example configuration in [nexus3.yaml.example](./nexus3.yaml.example)
to `/opt/stackstorm/configs/nexus3.yaml` and edit as required.

add nexus3 server connection profile:

* ``url`` - URL of the pack (e.g. ``https://myproject.abc.net``)
* ``user`` - username
* ``password`` - Password
* ``verify`` - https tls verify


**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`


## Actions

* **list_repositories** : List nexus3 repositories
* **get_repositories** : get nexus3 repositories
* **create_repositories** : create nexus3 repository
* **delete_repositories** : delete nexus3 repository

* **list_scripts** : List nexus3 scripts
* **get_scripts** : get nexus3 scripts
* **create_scripts** : create if missing, nexus3 script
* **delete_scripts** : delete nexus3 script

## Aliases


## Rules


## Sensors


## Policies


* **http.retry** : Retry core.http action on timeout.


