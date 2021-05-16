import requests

s = requests.Session()

host = "ios-xe-mgmt.cisco.com"
rest_path = "restconf"
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

url = f"https://{host}:{port}/{rest_path}/"

resp = s.get(url)

if resp.status_code == 200:
    print(resp.json())
else:
    print(f"Failed to retrieve information. Status code: {resp.status_code}")