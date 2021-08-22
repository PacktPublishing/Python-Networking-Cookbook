import requests

s = requests.Session()

host = "<insert host>"
rest_path = "restconf"
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

url = f"https://{host}:{port}/{rest_path}/"

resp = s.get(url)

if resp.status_code == 200:
    print(resp.json())
else:
    print(f"Failed to retrieve information. Status code: {resp.status_code}")