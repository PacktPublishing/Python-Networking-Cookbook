from genie.testbed import load
from genie.utils.diff import Diff
import json

testbed = load('testbed.yaml')
device = testbed.devices['csr1000v-1']
device.connect()

# Only learning interface here to keep demo short
current = device.learn('interface')

with open('backup.txt') as fh:
    snapshot = json.load(fh)

diff = Diff(snapshot, current.to_dict())
diff.findDiff()
print(diff)