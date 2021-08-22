import ipaddress
from jinja2 import Environment, FileSystemLoader
loader = FileSystemLoader("templates")
environment = Environment(loader=loader)

def to_ipv6(addr):
	raw_ipv4 = "2002::" + str(addr)
	ipv6 = ipaddress.IPv6Address(raw_ipv4)
	
	return str(ipv6)

environment.filters["toIPv6"] = to_ipv6

tpl = environment.get_template("filter.conf.tpl")

addresses = ["10.10.2.10", "10.10.2.40"]
out = tpl.render(addresses=addresses)
print(out)
