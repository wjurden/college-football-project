#===============================
# Using REQUESTS to pull the data
#===============================

# Change working directory to 'code' directory so creds can be passed
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/code')

# Importing packages
import creds
import os
import requests
import json
import pandas as pd

#===============================
# Pulling Data for Regular Season
#===============================

i = 0
# Configuring API
years = [2019,2020,2021,2022]
rows = []
df = pd.DataFrame()

for year in years: 
    endpoint = f'https://api.collegefootballdata.com/stats/player/season?year={year}' 
    headers = {"Authorization": f"Bearer {creds.api_key}"}

    # Requesting data
    response = requests.get(endpoint,headers=headers)
    json_response = response.json()

    # Pretty print
    print(json.dumps(json_response, indent=2))

    # Pulling keys of first list object to be the column names
    column_names = json_response[1].keys()

    if i == 0:
        # Pulling data from rows
        rows = [list(game.values()) for game in json_response]

        # Add year to list
        for row in rows:
            row.append(year)
    else: 
        # Pulling data from rows
        rows2 = [list(game.values()) for game in json_response]

        # Add year to list & then add the value to the main dataframe 
        for row in rows2:
            row.append(year)
            rows.append(row)
    
    # Iterate rows
    i += 1

# Convert column names to list & add year header
names = list(column_names)
names.append('year')

# Creating empty dataframe to add values into
df = pd.DataFrame(rows, columns=names)

# View data
df.head()
df.tail()

# Changing directory and then saving file
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/raw')
df.to_csv('raw_player_season_stats.csv', index= False)
