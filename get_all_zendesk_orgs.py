#import all necessary modules

import requests
import csv
import json

#define endpoint, headers, and session
#In header I have replace auth-token with your credentials, I used postman to create mine but you may use your own method

url = "https://ntv.zendesk.com/api/v2/organizations.json"
headers = {
                "Content-Type": "application/json",
                "Authorization": "Basic [auth-token]",
                "Accept": "application/json",
            }
s = requests.Session()

#loop through get request for orgainzations until the 'next-page' is null, this will make sure all orgs are written into csv file without having to make multiple requests

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

