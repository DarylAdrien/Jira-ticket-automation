# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://daryl.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth("daryl.adriene111@ptuniv.edu.in", "ATATT3xFfGF06rcdM2t9ebl7DSHBDzUroRd0j_b6rhvmyNfeUOwj7kAoiFl6u8yBca4jZFv9cWP2DOjNuBdLHY0swHsbnxkI-nzt_5L8VYYnmuf5eIa1linvkgtwoBN2v6amHnt-1llkkvSzENxu5nL_-2mhxYDm9aw3wG_wltyGlmKT_-tVVTA=2521A579")

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}


payload = json.dumps( {
  "fields": {


    "issuetype": {
      "id": "10009"
    },

    "project": {
      "key": "TEST"
    },

    "summary": "Main order flow broken",
  },
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))