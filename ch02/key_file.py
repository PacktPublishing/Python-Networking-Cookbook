from paramiko.client import SSHClient

# Credentials here are for a always-on Sandbox from Cisco DevNet
SSH_USER = "<Insert user>"
SSH_PASSWORD = "<insert password>"
SSH_HOST = "<insert host>"
SSH_PORT = 22
SSH_KEY = "<insert path to ssh key here>"
SSH_KEY_PASSWORD = "<insert ssh keyphrase here>"

client = SSHClient()
client.load_system_host_keys()
client.connect(SSH_HOST, port=SSH_PORT,
                         username=SSH_USER,
                         look_for_keys=True,
                         key_filename=SSH_KEY,
                         passphrase=SSH_KEY_PASSWORD)
stdin, stdout, stderr = client.exec_command('show ip interface brief')
client.close()