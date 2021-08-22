import os
import sys
import requests

base_url = "https://api.meraki.com/api/v1"
key = os.environ.get("MERAKI_DASHBOARD_API_KEY", None)

if key is None:
    print("Please provide an API key. Aborting.")
    sys.exit(-1)

sess = requests.Session()
sess.headers.update({
    "X-Cisco-Meraki-API-Key": key
})

url = f"{base_url}/organizations"

resp = sess.get(url)

if resp.status_code == 200:
    data = resp.json()

    for org in data:
        print(org['name'])
else:
    print(f"Bad response. Status code: {resp.status_code}")