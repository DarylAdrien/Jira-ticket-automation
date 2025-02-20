import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://daryl.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth("daryl.adriene111@ptuniv.edu.in", "ATATT3xFfGF0OcwJdUUhQEVWePEuoaS7oAXg7yk7WGy1Y3iDOKysC-924ZwI2FeV5WOTv0M6i7XZJwVAa6JFKpPaxY4_KqQD0cgzQctdij8ONZzKqy4W9gs_x5w-qG-Pcrq0Y0L-HxjdqcF8BbgfcHbfohInVw5ATGrFs4XxFt-JRCGw-EdNAGc=912C5540")

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

