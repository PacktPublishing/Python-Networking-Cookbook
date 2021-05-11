from pyats.topology import loader
testbed = loader.load('testbed.yaml')

device = testbed.devices['csr1000-v1']
device.connect()
out = device.execute("show ip interface brief")
print(out)