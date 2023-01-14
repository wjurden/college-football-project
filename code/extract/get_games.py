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
# Pulling Data for Regular Season
#===============================

# Configuring API
endpoint = 'https://api.collegefootballdata.com/games?year=2022' #Setting year to 2022
headers = {"Authorization": f"Bearer {creds.api_key}"}

# Requesting data
response = requests.get(endpoint,headers=headers)
json_response = response.json()

# Pretty print
print(json.dumps(json_response, indent=2))

# Pulling keys of first list object to be the column names
column_names = json_response[1].keys()

# Pulling data from rows
rows = [list(game.values()) for game in json_response]

# Creating empty dataframe to add values into
df = pd.DataFrame(rows, columns= column_names)

df.tail() # Checkpoint

#===============================
# Pulling Data for Post Season
#===============================

# Pull data for post season
ps_endpoint = 'https://api.collegefootballdata.com/games?seasonType=postseason&year=2022' #Setting year to 2022
response = requests.get(ps_endpoint,headers=headers)
json_response2 = response.json()

print(json.dumps(json_response2, indent=2)) # Checkpoint

# Extract values from dictionaries in json_response
rows2 = [list(game.values()) for game in json_response2]

# Creating second dataframe
df2 = pd.DataFrame(rows2, columns=column_names)

# Concat regular season and post season data
result = pd.concat([df, df2], ignore_index=True)

result.tail() # Checkpoint

#===============================
# Saving file
#===============================

# Changing directory and then saving file
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/raw')
result.to_csv('raw_game_data_2022.csv', index= False)