import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://xxx.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth("", "")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)
for i in range(len(output)):

    print(f"Project {i+1} : {output[i]["name"]}")

