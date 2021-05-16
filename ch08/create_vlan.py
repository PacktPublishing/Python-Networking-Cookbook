import requests
from pprint import pprint

protocol = "https"
host = "ios-xe-mgmt.cisco.com"
rest_path = "restconf/data"
port = 9443
user = "developer"
password = "C1sco12345"

s = requests.Session()
s.auth = (user, password)
s.headers.update({
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json"
})
s.verify = False

url = f"{protocol}://{host}:{port}/{rest_path}/ios-xe-native:native/vlan"

resp = s.get(url)

if resp.status_code == 200:
    pprint(resp.json())
else:
    print(f"Failed to retrieve data from device. Status code: {resp.status_code}")