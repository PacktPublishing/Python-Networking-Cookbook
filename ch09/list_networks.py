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

# Retrieve organizations
orgs_url = f"{base_url}/organizations"

resp_orgs = sess.get(orgs_url)

if resp_orgs.status_code == 200:
    for org in resp_orgs.json():
        org_id = org['id']
        print(f"Retrieving networks for {org['name']}")
        # Retrieve all networks
        url = f"{base_url}/organizations/{org_id}/networks"

        resp = sess.get(url)

        if resp.status_code == 200:
            for ntwrk in resp.json():
                print(f"- {ntwrk['name']}")
        else:
            print(f"Failed to retrieve network. Status code: {resp.status_code}")
else:
    print(f"Failed to retrieve orgs. Response code: {resp_orgs.status_code}")