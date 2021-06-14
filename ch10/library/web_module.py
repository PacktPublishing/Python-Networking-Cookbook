from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url
import json

DOCUMENTATION = r'''
---
module: web_module
short_description: A small module to retrieve all orgs from the meraki API.
version_added: "1.0.0."
description: Retrieve all organizations the user has access to.

options:
    access_token:
        description: The API access token to use
        required: true
        type: str
    base_url:
        description: The base url of the meraki API to use
        required: false
        default: https://api.meraki.com/api/v1
        type: str

author:
    - Name (GitHub handle)
'''

EXAMPLES = r'''
- name: Retrieving all my organizations from meraki
	  web_module:
        access_token: <Insert access token here>
'''

RETURN = r'''
status:
    description: The returned http status
    type: int
    returned: always
    sample: 200
organizations:
    description: A list of dictionaries describing the organizations
    type: list
    returned: success
    sample: [{"id": "463308", "name": "DevNet San Jose", "url": "https://n18.meraki.com/o/vB2D8a/manage/organization/overview"},]
'''
def run_module():
    args = {
        "access_token": {
            "required": True,
            "type": str
        },
        "base_url": {
            "required": False,
            "default": "https://api.meraki.com/api/v1",
            "type": str
        }
    }

    module = AnsibleModule(
        argument_spec=args,
        supports_check_mode=False
    )

    headers = {
        "X-Cisco-Meraki-API-Key": module.params['access_token']
    }

    url = "{}/organizations".format(module.params['base_url'])
    resp, info = fetch_url(module, url, method="get", headers=headers)

    result = {
        "changed": False,
        "status": info['status'],
    }

    if info['status'] == 200:
        result["networks"] = json.loads(resp.read())
        module.exit_json(**result)
    else:
        result["msg"] = "Unable to call API."
        module.fail_json(**result)

if __name__ == '__main__':
    run_module()
