from jinja2 import Environment, FileSystemLoader
loader = FileSystemLoader("templates")
environment = Environment(loader=loader)

tpl = environment.get_template("vars.conf.tpl")

user_name = input("What’s your name?: ")
tpl.stream(name=user_name).dump("rendered.conf")
