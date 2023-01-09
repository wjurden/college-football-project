#===============================
# Using REQUESTS to pull the data instead of custon CFDB package
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
endpoint = 'https://api.collegefootballdata.com/games?year=2022' #Setting year to 2022
headers = {"Authorization": f"Bearer {creds.api_key}"}

#===============================
# Pulling Data
#===============================
response = requests.get(endpoint,headers=headers)
json_response = response.json()

# Pretty print
print(json.dumps(json_response, indent=2))

#===============================
# Creating List of Values
#===============================

# Pulling keys of first list object
column_names = json_response[1].keys()

# Creating empty dataframe to add values into
df = pd.DataFrame(columns= column_names)

# Adding games to dataframe
for game in json_response:
    df.loc[len(df)] = game.values()

#===============================
# Saving file
#===============================

# Changing directory and then saving file
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/raw')
df.to_csv('raw_game_data_2022_requests.csv', index= False)