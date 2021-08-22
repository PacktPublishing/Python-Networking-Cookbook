import requests
from pprint import pprint

protocol = "https"
host = "10.10.20.48"
rest_path = "restconf/data"
port = 443
user = "<insert user>"
password = "<insert password>"

s = requests.Session()
s.auth = (user, password)
s.headers.update({
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json"
})
s.verify = False

url = f"{protocol}://{host}:{port}/{rest_path}/ietf-interfaces:interfaces"

resp = s.get(url)

if resp.status_code == 200:
    pprint(resp.json())
else:
    print(f"Failed to retrieve data from device. Status code: {resp.status_code}")