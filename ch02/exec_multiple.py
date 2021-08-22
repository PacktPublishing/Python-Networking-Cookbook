import json
from paramiko.client import SSHClient

credentials = {}
with open("credentials.json") as fh:
    credentials = json.load(fh)

CMD = "show running-config"
for cred in credentials:
	out_file_name = str(cred['name']) + ".txt"
	client = SSHClient()
	client.load_system_host_keys()
	client.connect(cred['host'], port=cred['port'],
                              username=cred['username'],
                              password=cred['password'])
	stdin, stdout, stderr = client.exec_command(CMD)
	
	out_file = open(out_file_name, "w")
	output = stdout.readlines()
	for line in output:
		out_file.write(line)
	out_file.close()
	client.close()
	print("Executed command on " + cred['name'])
