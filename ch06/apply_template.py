import napalm
from jinja2 import Environment, FileSystemLoader

# Generate template
loader = FileSystemLoader("templates")
environment = Environment(loader=loader)

tpl = environment.get_template("acl.conf.tpl")

allowed = [
	"10.10.0.10",
	"10.10.0.11",
	"10.10.0.12"
]
disallowed = [
	"10.10.0.50",
	"10.10.0.62"
]
intf = "ethernet0"

out = tpl.render(allowed=allowed, disallowed=disallowed, intf=intf)

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
device.load_merge_candidate(config=out)
print(device.compare_config())

user_inp = input("Do you want to apply the changes?[y/n] ")
if user_inp == "y":
    device.commit_conifg()
else:
    device.discard_config()
device.close()