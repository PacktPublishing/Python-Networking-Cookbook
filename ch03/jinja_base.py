from jinja2 import Environment, FileSystemLoader
loader = FileSystemLoader("templates")
environment = Environment(loader=loader)

tpl = environment.get_template("child.conf.tpl")

out = tpl.render()
print(out)
