from netmiko import ConnectHandler, file_transfer

connection_info = {
    'device_type': 'cisco_ios',
    'host': '<insert host>',
    'port': 22,
    'use_keys': True,
    'key_file': '<insert path to key file>',
    'username': '<insert username>'
}

with ConnectHandler(**connection_info) as conn:
    out = conn.send_command("show interfaces")
    print(out)