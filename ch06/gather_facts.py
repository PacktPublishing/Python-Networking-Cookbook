import napalm

driver = napalm.get_network_driver("ios")

conn_details = {
    "hostname" : 'ios-xe-mgmt.cisco.com',
    "username" : 'developer',
    "password" : 'C1sco12345',
    "optional_args": {
        "port": 8181
    }
}

device = driver(**conn_details)
device.open()
interfaces = device.get_interfaces()
facts = device.get_facts()
print(facts)
device.close()
