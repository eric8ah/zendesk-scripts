# This is a script to update a custom field for existing Zendesk organizations using a csv file containing their ids and the field ValueError
# In my case it was a custom field to import the salesforce ID

import requests
import csv
import json

#split the endpoint in two so you can insert the Zendesk org in between per iteration
url1 = "https://ntv.zendesk.com/api/v2/organizations/"
id = ''
salesforce_id = ''
url2 = ".json"
headers = {
                "Content-Type": "application/json",
                "Authorization": "Basic ZW9jaG9hQG5hdGl2by5jb206TW9vc2UhQCMhQCM0",
                "Accept": "application/json"
            }

open_file = open('zendesk_salesforce.csv', 'r')
csv_file = csv.reader(open_file)

def get_headers(csv_file):
		header = next(csv_file)
		return map((lambda x: x), header)

csv_headers = get_headers(csv_file)
id_index = csv_headers.index('id')
salesforce_id_index = csv_headers.index('salesforceID')

#loop through the csv file updating the id & salesforce ID and making a put request per iteration
for row in csv_file:
	id = row[id_index]
	salesforce_id = row[salesforce_id_index]
	urlFull = urlFull = url1 + id + url2

	data = {
		"organization": {
			"organization_fields": {
				"salesforce_account_id": salesforce_id
					}
			}
		}

	payload = json.dumps(data)
	response = requests.put(urlFull, data=payload, headers=headers)

	print(id)
	print(salesforce_id)
	print(payload)
	print(response)
