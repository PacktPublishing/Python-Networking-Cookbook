from ansible.module_utils.basic import AnsibleModule
import ipaddress

DOCUMENTATION = r'''
---
module: value_module
short_description: A small module to create IPv4 address list.
version_added: "1.0.0."
description: Create a IPv4 address list based on host portion and netmask information.

options:
    ip_address:
        description: The network portion of your IP
        required: true
        type: str
    netmask:
        description: The netmask of your IP address pool
        required: true
        type: int

author:
    - Name (GitHub handle)
'''

EXAMPLES = r'''
- name: Testing my ip address task
	  value_module:
        ip_address: 192.168.10.0
        netmask: 28
'''

RETURN = r'''
addressses:
    description: A list of IPv4 addresses
    type: list
    returned: always
    sample: ['192.168.10.1', '192.168.10.2']
'''
def run_module():
    args = {
        "ip_address": {
            "type": str,
            "required": True
        },
        "netmask": {
            "type": int,
            "required": True
        }
    }

    module = AnsibleModule(
        argument_spec=args,
        supports_check_mode=False
    )

    # Generate IP addresses
    cidr_address = str(module.params['ip_address']) + "/" + str(module.params['netmask'])

    address_objects = ipaddress.IPv4Network(unicode(cidr_address))

    addresses = []
    for a in address_objects:
        addresses.append(str(a))
    result = {
        "changed": False,
        "addresses": addresses
    }
    module.exit_json(**result)

if __name__ == '__main__':
    run_module()
