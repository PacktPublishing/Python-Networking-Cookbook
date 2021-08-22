from paramiko.client import SSHClient

# Credentials here are for a always-on Sandbox from Cisco DevNet
SSH_USER = "<Insert your ssh user here>"
SSH_PASSWORD = "<Insert your ssh password here>"
SSH_HOST = "<Insert the IP/host of your device/server here>"
SSH_PORT = 22 # Change this if your SSH port is different

client = SSHClient()
client.load_system_host_keys()

try:
    client.connect(SSH_HOST, port=SSH_PORT,
                             username=SSH_USER,
                             password=SSH_PASSWORD,
                             look_for_keys=False)
    print("Connected succesfully!")
except Exception:
    print("Failed to establish connection.")
finally:
    client.close()