from pyats.topology import loader
from genie.conf.base import Interface

testbed = loader.load('testbed.yaml')
device = testbed.devices['csr1000v-1']
device.connect()

intf = Interface(device=device, name='GigabitEthernet2')

intf.ipv4 = '10.10.10.2'
intf.ipv4.netmask = '255.255.255.0'
intf.shutdown = False

intf.build_config()