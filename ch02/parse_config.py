from paramiko.client import SSHClient
from paramiko import SSHConfig

SSH_CONFIG = "<insert path to ssh config>"
SSH_HOST = "example"

config = SSHConfig()
config_file = open(SSH_CONFIG)

config.parse(config_file)

dev_config = config.lookup(SSH_HOST)

client = SSHClient()
client.load_system_host_keys()

HOST = dev_config['hostname']

client.connect(HOST, port=int(dev_config['port']),
                     username=dev_config['user'],
                     password=dev_config['password'])
client.close()