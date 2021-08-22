import requests
import pprint

protocol = "https"
host = "<insert host>"
rest_path = "restconf/data"
port = 443 # change port if needed
user = "<insert user>"
password = "<insert password>"

s = requests.Session()
s.auth = (user, password)
s.verify = False
s.headers.update({
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json"
})

intf_name = "GigabitEthernet=2"
url = f"https://{host}:{port}/{rest_path}/ios-xe-native:native/interface/{intf_name}"

payload = {
    "name": "3.10",
    "encapsulation": {
        'dot1Q': {
            'vlan-id': 10
        }
    }
}

resp = s.post(url, json=payload)

if resp.status_code == 200:
    pprint.pprint(resp.json())
else:
    print(f"Failed to retrieve data from device. Status code: {resp.status_code} {resp.content}")