import pprint
from netmiko import ConnectHandler

connection_info = {
    'device_type': 'cisco_ios',
    'host': 'ios-xe-mgmt.cisco.com',
    'port': 8181,
    'username': 'developer',
    'password': 'C1sco12345'
}

with ConnectHandler(**connection_info) as conn:
    out = conn.send_command("show running-config", use_genie=True)
    print(out)