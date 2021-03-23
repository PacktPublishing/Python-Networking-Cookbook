from jinja2 import Environment, FileSystemLoader
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
print(out)
