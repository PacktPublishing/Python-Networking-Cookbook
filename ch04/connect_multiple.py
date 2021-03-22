import json
from netmiko import ConnectHandler

devices = []
with open("connections.json", "r") as fh:
    devices = json.load(fh)

CMD = "show running-config"

for device in devices:
    file_name = f"{device['name']}.out"
    print(f"Retrieving config for {device['name']}")
    with ConnectHandler(**device['connection']) as conn:
        out = conn.send_command(CMD)

        with open(file_name, "w") as f:
            f.write(out)
    