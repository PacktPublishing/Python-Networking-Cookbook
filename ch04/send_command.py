import pprint
from netmiko import ConnectHandler

connection_info = {
    'device_type': 'cisco_ios',
    'host': '<insert host>',
    'port': 22, # Change if your port is different
    'username': '<insert username>',
    'password': '<insert password>'
}

with ConnectHandler(**connection_info) as conn:
    out = conn.send_command("show running-config")
    print(out)