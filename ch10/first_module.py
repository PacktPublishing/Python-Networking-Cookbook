from ansible.module_utils.basic import AnsibleModule

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
