from ncclient import manager
conn_info = {
    "host": "<insert host>",
    "port": 830, # change port
    "username": "<insert username>",
    "password": "<insert password>",
    "hostkey_verify": False
}

device = manager.connect(**conn_info)
device.copy_config(source='running', target='file:///now_running.conf')
device.copy_config(source='file:///now_running.conf', target='starting')