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
intf = "Loopback10"

out = tpl.render(allowed=allowed, disallowed=disallowed, intf=intf)

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
device.load_merge_candidate(config=out)
device.commit_config()
device.close()