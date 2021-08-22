from ncclient import manager
conn_info = {
    "host": "10.10.20.48",
    "port": 830,
    "username": "developer",
    "password": "C1sco12345",
    "hostkey_verify": False
}

device = manager.connect(**conn_info)

capabilities = device.server_capabilities

for cap in capabilities:
    if "http://openconfig.net/yang/" in cap:
        print(cap)