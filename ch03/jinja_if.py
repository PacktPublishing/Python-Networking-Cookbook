from jinja2 import Environment, FileSystemLoader
loader = FileSystemLoader("templates")
environment = Environment(loader=loader)

tpl = environment.get_template("ports.conf.tpl")

ports = []
port_1 = {
	"type": "ethernet",
	"slot": 1,
	"port_num": 1,
	"intf_type": "access"
}
ports.append(port_1)

port_2 = {
	"type": "ethernet",
	"slot": 1,
	"port_num": 1,
	"intf_type": "trunk"
}
ports.append(port_2)

out = tpl.render(ports=ports)
print(out)
