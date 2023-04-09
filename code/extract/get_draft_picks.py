#===============================
# Using REQUESTS to pull the data
#===============================

# Importing packages
import creds
import os
import requests
import json
import pandas as pd

# Change working directory to 'code' directory so creds can be passed
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/code')

#===============================
# Configuring API
#===============================
endpoint = 'https://api.collegefootballdata.com/draft/picks?year=2022' #Setting year to 2022
headers = {"Authorization": f"Bearer {creds.api_key}"}

#===============================
# Pulling Data
#===============================
response = requests.get(endpoint,headers=headers)
json_response = response.json()

# Pretty print
print(json.dumps(json_response, indent=2))

# Extract values from dictionaries in json_response
rows = [list(play.values()) for play in json_response]

# Pulling keys of first list object
column_names = json_response[1].keys()
df = pd.DataFrame(rows, columns=column_names)

# Drop hometown info=
df.drop(columns='hometownInfo', inplace=True)

#===============================
# Saving file
#===============================

# Changing directory and then saving file
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/raw')
df.to_csv('raw_draft_picks_2022.csv', index= False)


