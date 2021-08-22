from paramiko.client import SSHClient
import time

# Credentials here are for a always-on Sandbox from Cisco DevNet
SSH_USER = "<Insert user>"
SSH_PASSWORD = "<insert password>"
SSH_HOST = "<insert host>"
SSH_PORT = 22 # Change this if your SSH port is differente

client = SSHClient()
client.load_system_host_keys()


client.connect(SSH_HOST, port=SSH_PORT,
                         username=SSH_USER,
                         password=SSH_PASSWORD,
                         look_for_keys=False)

channel = client.get_transport().open_session()
shell = client.invoke_shell()

commands = [
	"configure terminal",
	"hostname test"
]

for cmd in commands:
      shell.send(cmd + "\n")
      out = shell.recv(1024)
      print(out)
      time.sleep(5)
