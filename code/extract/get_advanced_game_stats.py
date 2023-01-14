#===============================
# NOT SURE I ACTUALLY NEED THESE DATA.... 
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
endpoint = 'https://api.collegefootballdata.com/stats/game/advanced?year=2022&seasonType=both' #Setting year to 2022 & season to both
headers = {"Authorization": f"Bearer {creds.api_key}"}

# Requesting data
response = requests.get(endpoint,headers=headers)
json_response = response.json()

# Pretty print
print(json.dumps(json_response, indent=2))

#===============================
#===============================
# Everything below this needs to be reworked due to the strcture of the JSON
#===============================
#===============================

# Pulling keys of first list object to be the column names
column_names = json_response[1].keys()

# Pulling data from rows
rows = [list(game.values()) for game in json_response]

# Creating empty dataframe to add values into
df = pd.DataFrame(rows, columns= column_names)

df.tail() # Checkpoint


# Test string 
jsonString = json.dumps(json_response)

df = pd.read_json(jsonString)
df2 = df.iloc[:,0:4]

# Unpacking offensive data
off_df = df['offense'].apply(pd.Series)
df3 = off_df.iloc[:,0:14]

ostd_df = off_df['standardDowns'].apply(pd.Series)
opass_df = off_df['passingDowns'].apply(pd.Series)
orush_df = off_df['rushingPlays'].apply(pd.Series)
opp_df = off_df['passingPlays'].apply(pd.Series)

# Unpacking defensive data
def_df = df['defense'].apply(pd.Series)
df4 = def_df.iloc[:,0:14]

dpass_df = off_df['standardDowns'].apply(pd.Series)
dpass_df = off_df['passingDowns'].apply(pd.Series)
drush_df = off_df['rushingPlays'].apply(pd.Series)
dpp_df = off_df['passingPlays'].apply(pd.Series)

# Pretty print
print(json.dumps(json_response, indent=2))