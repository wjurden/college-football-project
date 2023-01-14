#===============================
# WORK IN PROGRESS
#===============================

# Importing packages
import creds
import os
import requests
import pandas as pd
from datetime import datetime 
import json

# Change working directory to 'code' directory so creds can be passed
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/code')

#===============================
# Configuring API
#===============================

# Creating a list of week numbers that will be looped through
week = list(range(1,15))

# Configuring the api header
headers = {"Authorization": f"Bearer {creds.api_key}"}


#===============================
# Testing response
#===============================

endpoint = f'https://api.collegefootballdata.com/games/players?year=2022&week=1&seasonType=regular&team=Ohio%20State' 
response = requests.get(endpoint,headers=headers)
json_response = response.json()

print(json.dumps(json_response, indent=2)) # Checkpoint

#===============================
# Unpacking json
#===============================

# This is the root of each school
osu = json_response[0]['teams'][1]
osu_cat = json_response[0]['teams'][1]['categories']

json_response[0]['teams'][1]['categories'][0]

#===============================
# Saving file
#===============================

# Changing directory and then saving file
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/raw')
result2.to_csv('raw_player_game_data_2022.csv', index= False)