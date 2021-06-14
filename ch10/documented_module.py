from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = r'''
---
module: documented_module
short_description: A small documented module.
version_added: "1.0.0."
description: This is a longer description of our documented module.

author:
    - Name (GitHub handle)
'''

EXAMPLES = r'''
- name: Testing my documented task
	  documented_module
'''

RETURN = r'''
message:
    description: A small welcome message returned by our module
    type: str
    returned: always
    sample: 'Hello from my first ansible module'
'''
def run_module():
    args = {}
    result = {
        "changed": False,
        "messsage": 'Hello from my first ansible module'
    }

    module = AnsibleModule(
        argument_spec=args,
        supports_check_mode=False
    )
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
