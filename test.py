#2 params
#1header

import requests
import json

body = {'username': "Anuvrat", 'password': "password"}

resp = requests.post(url="some url", body=body)

#resp_json_in_str = json.loads(resp)
session_id = resp.content['session_id']

resp2 = requests.post(url = "some other url", header= session_id)
check = resp2.status_code
