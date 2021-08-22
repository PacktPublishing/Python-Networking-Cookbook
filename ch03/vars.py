from jinja2 import Environment, FileSystemLoader
loader = FileSystemLoader("templates")
environment = Environment(loader=loader)

tpl = environment.get_template("vars.conf.tpl")

user_name = input("What’s your name?: ")
out = tpl.render(name=user_name)
print(out)
