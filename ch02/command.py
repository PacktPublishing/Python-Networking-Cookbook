import time
from paramiko.client import SSHClient

# Credentials here are for a always-on Sandbox from Cisco DevNet
SSH_USER = "<Insert user>"
SSH_PASSWORD = "<insert password>"
SSH_HOST = "<insert host>"
SSH_PORT = 22 # Change this if your SSH port is different

client = SSHClient()
client.load_system_host_keys()


client.connect(SSH_HOST, port=SSH_PORT,
                         username=SSH_USER,
                         password=SSH_PASSWORD,
                         look_for_keys=False)

CMD = "show ip interface brief" # You can issue any command you want
stdin, stdout, stderr = client.exec_command(CMD)
time.sleep(5)

client.close()
