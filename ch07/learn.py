import json
from genie.testbed import load

testbed = load('testbed.yaml')

device = testbed.devices['csr1000v-1']
device.connect()

# Only learning interface here to keep demo short
output = device.learn('interface')
with open("backup.txt", "w") as fh:
    json.dump(output.to_dict(), fh, indent=2)