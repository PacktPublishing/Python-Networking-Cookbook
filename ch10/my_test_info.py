#!/usr/bin/python

# Copyright: (c) 2020, Your Name <YourName@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#from __future__ import (absolute_import, division, print_function)

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

if __name__ == '__main__':
    run_module()
