from paramiko.client import SSHClient

SSH_USER = "<Insert your ssh user here>"
SSH_HOST = "<Insert the IP/host of your device/server here>"
SSH_PORT = 22 # Change this if your SSH port is different
SSH_KEY = "<Insert the name of your private key here>"
SSH_KEY_PASSWORD = "<Insert the password here>"

client = SSHClient()
client.load_system_host_keys()
client.connect(SSH_HOST, port=SSH_PORT,
                         username=SSH_USER,
                         look_for_keys=True,
                         key_filename=SSH_KEY,
                         passphrase=SSH_KEY_PASSWORD)
stdin, stdout, stderr = client.exec_command('<your command>')
client.close()