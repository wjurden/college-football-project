#===============================
# Using REQUESTS to pull the data instead of custon CFDB package
#===============================

#Importing packages
import creds
import os
import requests
import json

#Change working directory to 'code' directory so creds can be passed
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/code')

#===============================
# Configuring API
#===============================
endpoint = 'https://api.collegefootballdata.com/games?year=2022' #Setting year to 2022
headers = {"Authorization": f"Bearer {creds.api_key}"}

#===============================
# Creating an instance of the API for all games in 2022
#===============================
response = requests.get(endpoint,headers=headers)
json_response = response.json()

#Pretty print
print(json.dumps(json_response, indent=2))

# Printing keys of first list object
json_response[1].keys()

#===============================
# Creating List of Values
#===============================