from netmiko import ConnectHandler
import pprint

connection_info = {
    'device_type': 'cisco_ios',
    'host': '<insert host>',
    'port': 22, # Change if your port is different
    'username': '<insert username>',
    'password': '<insert password>'
}

with ConnectHandler(**connection_info) as conn:
    out = conn.send_command("show interfaces", use_genie=True)
    pprint.pprint(out)
    for interface in out.keys():
        print(interface)