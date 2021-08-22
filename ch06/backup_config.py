import napalm

driver = napalm.get_network_driver("ios")

conn_details = {
    "hostname" : 'sandbox-iosxe-recomm-1.cisco.com',
    "username" : 'developer',
    "password" : 'C1sco12345',
    "optional_args": {
        "port": 22
    }
}

device = driver(**conn_details)
device.open()
config = device.get_config()

host = conn_details['hostname']
for conf_type in config.keys():
    with open(f"{host}-{conf_type}.conf.bak", "w") as f:
        f.writelines(config[conf_type])
device.close()