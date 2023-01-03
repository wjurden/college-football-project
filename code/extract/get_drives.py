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
endpoint = 'https://api.collegefootballdata.com/drives?year=2022' #Setting year to 2022
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

# Adding data to dataframe
for drive in json_response:
    df.loc[len(df)] = drive.values()

# Converting time values to seconds
i = 0
while i < len(json_response):
    df.loc[i,'start_time_sec'] = round(json_response[i]['start_time']['minutes']*60 + json_response[i]['start_time']['seconds'])
    df.loc[i,'end_time_sec'] = round(json_response[i]['end_time']['minutes']*60 + json_response[i]['end_time']['seconds'])
    df.loc[i,'elapsed_sec'] = round(json_response[i]['elapsed']['minutes']*60 + json_response[i]['elapsed']['seconds'])
    i += 1

#===============================
# Saving file
#===============================

# Changing directory and then saving file
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/raw')
df.to_csv('raw_drive_data_2022.csv', index= False)