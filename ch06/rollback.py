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
config_change = [
    "hostname test"
]
new_config = "\n".join(config_change)
device.load_merge_candidate(config=new_config)
print(device.compare_config())

user_in = input("Continue? [y/n]")
if user_in == "y":
    device.commit_conifg()
    print("Applied config to the device")
else:
    device.rollback()
    print("Rolled back to previous config")
device.close()
