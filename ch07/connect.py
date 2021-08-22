from pyats.topology import loader
testbed = loader.load('testbed.yaml')

device = testbed.devices['csr1000v-1']
device.connect()
out = device.execute("show ip interface brief")
print(out)