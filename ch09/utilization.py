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
url = f"{base_url}/networks/{network_id}/networkHealth/channelUtilization"

params = {
    'timespan': 7
}
resp = sess.get(url, params=params)

if resp.status_code == 200:
    aps = resp.json()
    for ap in aps:
        print(f"Wifies on AP {ap['serial']}")
        for e in ap['wifi0']:
            print(f"{e['utilizationTotal']}")
else:
    print(f"Failed to retrieve utilization. Code: {resp.status_code}")