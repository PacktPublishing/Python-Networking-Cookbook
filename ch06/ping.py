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

to_ping = [
    "packtpub.com",
    "10.0.0.1"
]
for host in to_ping:
    res = device.ping(host)
    print(f"Results for {host}")
    print(res)

device.close()