import requests
import json
from datetime import datetime


now = datetime.now()
date_time = now.strftime('%Y_%m_%d_%H_%M_%S')

f = open(f"leapchain_polls_{date_time}.json", "w")
poll_backup = []

base_url = "https://7nfr0m.deta.dev"

polls = requests.get(f"{base_url}/api/v1/polls").json()

for poll in polls:
    poll_id = poll["_id"]
    print(f"Fetching details of poll with id {poll_id}")
    poll_details = requests.get(f"{base_url}/api/v1/polls/{poll_id}").json()
    poll_details["poll"]["votes"] = poll_details["votes"]
    new_poll_details = poll_details["poll"]
    poll_backup.append(new_poll_details)

f.write(json.dumps(poll_backup))
f.close()
