import requests
import json
import sys
from requests.auth import HTTPBasicAuth

base_url = "<insert ip or hostname of FMC>" # i.e. https://10.10.10.110

username = "<insert username>"
password = "<insert password>"

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

for d in domains:
    print(f"{d['name']}: {d['uuid']}")