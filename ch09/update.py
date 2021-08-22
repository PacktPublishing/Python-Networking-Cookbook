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

serial = os.environ.get("MERAKI_SERIAL")
port = 0
url = f"{base_url}/devices/{serial}/switch/ports/{port}"

resp = sess.get(url)
if resp.status_code == 200:
    conf = resp.json()
    conf['stickyMacAllowListLimit'] = 10

    resp_update = sess.put(url, json=conf)
    
    if resp_update.status_code == 200:
        print("Config updated!")
    else:
        print(f"Failed to update. Status: {resp_update.status_code}")
else:
    print(f"Failed to get config. Status: {resp.status_code}")