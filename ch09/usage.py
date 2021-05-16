import os
import sys
import csv
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
url = f"{base_url}/networks/{network_id}/clients"

resp = sess.get(url)

if resp.status_code == 200:
    clients = resp.json()

    with open('clients.csv', 'w') as csvfile:
        out = csv.writer(csvfile, delimiter=',')
        out.writerow(clients[0].keys())

        for client in clients:
            out.writerow(client.values())
else:
    print(f"Request failed. Status code: {resp.status_code}")
