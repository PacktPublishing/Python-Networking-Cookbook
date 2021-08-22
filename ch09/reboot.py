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

serial = "<insert serial>"
url = f"{base_url}/devices/{serial}/reboot

resp = sess.post(url)

if resp.status_code == 202:
    print("Rebooted device successfully.")
else:
    print(f"Failed to reboot device. Status code: {resp.status_code}")