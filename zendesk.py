import requests
import csv
import json

url = "https://ntv.zendesk.com/api/v2/organizations.json"
headers = {
                "Content-Type": "application/json",
                "Authorization": "Basic [auth-token]",
                "Accept": "application/json",
            }
s = requests.Session()

while url:
	response = s.get(url, headers=headers)
	data = response.json()
	org_data = data['organizations']
	url = data['next_page']
	if response.status_code != 200: 
		print("Status:", response.status_code, 'Problem with the request.')
		exit()
	f = open("All_ZD_Orgs.csv",'a')
	csvwriter = csv.writer(f)
	count = 0
	for org in org_data:
		if count == 0:
			header = org.keys()
			csvwriter.writerow(header)
			count += 1
		csvwriter.writerow(org.values())
	f.close()

