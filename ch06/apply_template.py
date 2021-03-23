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
device.load_merge_candidate(config='hostname test\n')
print(device.compare_config())

user_inp = input("Do you want to apply the changes?[y/n] ")
if user_inp == "y":
    device.commit_conifg()
else:
    device.discard_config()
device.close()