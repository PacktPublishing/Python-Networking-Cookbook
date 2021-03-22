from paramiko.client import SSHClient
import time

SSH_USER = "<Insert your ssh user here>"
SSH_PASSWORD = "<Insert your ssh password here>"
SSH_HOST = "<Insert the IP/host of your device/server here>"
SSH_PORT = 22 # Change this if your SSH port is different

client = SSHClient()
client.load_system_host_keys()


client.connect(SSH_HOST, port=SSH_PORT,
                         username=SSH_USER,
                         password=SSH_PASSWORD,
                         look_for_keys=False)

channel = client.get_transport().open_session()
shell = channel.invoke_shell()

commands = [
	"configure terminal",
	"hostname test"
]

for cmd in commands:
	shell.send(cmd + "\n")
      out = shell.recv(1024)
      print(out)
	time.sleep(1)
