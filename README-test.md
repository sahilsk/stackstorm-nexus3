## Testing locally


Copy component files
    
    cp -rf actions/*  /opt/stackstorm/packs/nexus3/actions/

If any *.yaml file is changed, run reload accordingly.

    st2ctl reload --register-configs
    st2ctl reload --register-actions
    st2ctl reload --register-rules


trigger Execution

    st2 action execute nexus3.list_repositories username="sahilsk" | grep "execution get"  | xargs -0 -I{} bash -c "sleep 2; {}"

Or better in a loop

  List Repository:

    while true; do mkdir -p /opt/stackstorm/packs/nexus3; cp -rf ./*  /opt/stackstorm/packs/nexus3/; chmod -R --reference /opt/stackstorm/packs/linux /opt/stackstorm/packs/nexus3; chown -R --reference /opt/stackstorm/packs/linux/pack.yaml /opt/stackstorm/packs/nexus3/*; st2 action execute nexus3.list_repositories username="sahilsk" | grep "execution get"  | xargs -0 -I{} bash -c "sleep 2; {}"; sleep 2; done;

  Create Repository

    while true; do mkdir -p /opt/stackstorm/packs/nexus3; cp -rf ./*  /opt/stackstorm/packs/nexus3/; chmod -R --reference /opt/stackstorm/packs/linux /opt/stackstorm/packs/nexus3; chown -R --reference /opt/stackstorm/packs/linux/pack.yaml /opt/stackstorm/packs/nexus3/*;  st2 action execute nexus3.create_repositories config_profile='dev' type=hosted name='maven2-dumy' format='maven2' write_policy='ALLOW'  | grep "execution get"  | xargs -0 -I{} bash -c "sleep 2; {}"; sleep 2; done;

  Delete Repository
  
    while true; do mkdir -p /opt/stackstorm/packs/nexus3; cp -rf ./*  /opt/stackstorm/packs/nexus3/; chmod -R --reference /opt/stackstorm/packs/linux /opt/stackstorm/packs/nexus3; chown -R --reference /opt/stackstorm/packs/linux/pack.yaml /opt/stackstorm/packs/nexus3/*;  st2 action execute nexus3.delete_repositories config_profile='dev' name='maven2-dumy' | grep "execution get"  | xargs -0 -I{} bash -c "sleep 2; {}"; sleep 2; done;


If any `yaml` file is updated , update it:

    #eg. updating action list_repositories.yaml
    st2 action update nexus3.list_repositories  ./actions/list_repositories.yaml

Last 2 executions

    st2 execution list  -n 2


``` json
{
  "success": true,
  "data": {
    "name": "dummy1",
    "type": "hosted",
    "format": "maven2",
    "recipe": "maven2-hosted",
    "online": true,
    "attributes": {
      "cleanup": {
        "policyName": "None"
      },
      "maven": {
        "versionPolicy": "RELEASE",
        "layoutPolicy": "STRICT"
      },
      "storage": {
        "strictContentTypeValidation": true,
        "writePolicy": "ALLOW_ONCE",
        "blobStoreName": "default"
      }
    },
    "url": "http://localhost:8081/repository/dummy1/",
    "status": {
      "repositoryName": "dummy1",
      "online": true,
      "description": null,
      "reason": null
    }
  }
}
``