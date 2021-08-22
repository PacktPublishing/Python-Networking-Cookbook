import requests
import json
import sys
from requests.auth import HTTPBasicAuth

base_url = "<insert ip or hostname of FMC>" # i.e. https://10.10.10.110

username = "<insert username>"
password = "<insert password>"
domain = "<insert domain>"
policy_id = '<insert policy id>'

def get_authenticated_session(user, password, base_url):
    auth_url = f"{base_url}/api/fmc_platform/v1/auth/generatetoken"
    auth = HTTPBasicAuth(user, password)

    resp = requests.post(auth_url, auth=auth, verify=False)

    s = requests.Session()
    if resp.ok:
        s.headers.update({
            'X-auth-access-token': resp.headers.get('X-auth-access-token')
        })
        s.verify = False
        print("Authenticated succesfully!")
        domains = json.loads(resp.headers.get('DOMAINS'))

        return s, domains
    else:
        print(f"Failed to authenticate. Response code: {resp.status_code}")
        sys.exit(-1)

sess, domains = get_authenticated_session(username, password, base_url)

url = f"{base_url}/api/fmc_config/v1/domain/{domain}/policy/accesspolicies/{policy_id}/accessrules"
resp = sess.get(url)

next_page = url

items = []
resp = sess.get(next_page)

if resp.ok:
    data = resp.json()

    for i in data['items']:
        items.append(i)
    next_links = []

    if "next" in data['paging']:
        if isinstance(data['paging']['next'], list):
            next_links = data['paging']['next']
        else:
            next_links.append(data['paging']['next'])

    for link in next_links:
        print(f"Requesting url '{link}'")
        resp = sess.get(link)

        if resp.ok:
            for i in resp.json()['items']:
                items.append(i)
        else:
            print(f"Failed to request url '{link}'. Status code: {resp.status_code}")
else:
    print(f"Failed to request url '{url}'. Status code: {resp.status_code}")

for i in items:
    url = i['links']['self']

    r = sess.get(url)
    if r.ok:
        rule = r.json()

        print(f"{rule['name']}({rule['id']}): Action: {rule['action']} Enabled: {rule['enabled']}")