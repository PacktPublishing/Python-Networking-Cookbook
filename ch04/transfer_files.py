from netmiko import ConnectHandler, file_transfer

connection_info = {
    'device_type': 'cisco_ios',
    'host': '<insert host>',
    'port': 22, # Change if your port is different
    'username': '<insert username>',
    'password': '<insert password>'
}

with ConnectHandler(**connection_info) as conn:
    ret = file_transfer(conn, source_file="test_upload.txt",
                              dest_file="test_on_device.txt",
                              file_system="flash:",
                              direction="put")
    
    for k, v in ret.items():
        print(f"{k}: {v}")