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

url = f"{base_url}/api/fmc_config/v1/domain/{domain}/policy/accesspolicies/{policy_id}"

resp = sess.get(url)
if resp.ok:
    data = resp.json()

    if 'urls' in data.keys():
        del data['urls']

    if 'metadata' in data.keys():
        del data['metadata']
    
    if 'links' in data.keys():
        del data['links']

    if 'rules' in data.keys():
        del data['rules']

    print(json.dumps(data, indent=2))
    data['name'] = 'Test-API'

    r = sess.put(url, json=data)
    print(r.status_code)
    print(data)