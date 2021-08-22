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

network_id = "L_783626335162466515"
url = f"{base_url}/networks/{network_id}/switch/qosRules"

resp = sess.get(url)
if resp.status_code == 200:
    rules = resp.json()
    for rule in rules:
        url_del = f"{base_url}/networks/{network_id}/switch/qosRules/{rule['id']}"
        resp_del = sess.delete(url_del)
        
        if resp_del.status_code == 204:
            print(f"Deleted QoS rule {rule['id']}")
        else:
            print(f"Failed on delete request. Status: {resp_del.status_code}")
else:
    print(f"Failed to retrieve rules. Status: {resp.status_code}")