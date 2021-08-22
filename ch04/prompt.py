from netmiko import ConnectHandler, file_transfer

connection_info = {
    'device_type': 'cisco_ios',
    'host': '<insert host>',
    'port': 22, # Change if your port is different
    'username': '<insert username>',
    'password': '<insert password>'
}

with ConnectHandler(**connection_info) as conn:
    conn.send_command("delete flash:/test_on_device.txt",
                        expect_string=r"Delete filename",
                        strip_prompt=False,
                        strip_command=False)
    
    conn.send_command("\n",
                        expect_string=r"confirm",
                        strip_prompt=False,
                        strip_command=False)
    
    conn.send_command("y",
                        expect_string=r"#",
                        strip_prompt=False,
                        strip_command=False)