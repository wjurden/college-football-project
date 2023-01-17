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

# Configuring the api header
headers = {"Authorization": f"Bearer {creds.api_key}"}

#===============================
# Unpacking json
#===============================

# Creating a list of week numbers that will be looped through
week = list(range(1,15))

# Creating column names
column_names = ['school', 'conference', 'homeAway', 'points', 'category', 'sub_category', 'athlete_id', 'athlete_name', 'stat']

# Creating empty data frame
df = pd.DataFrame(columns=column_names)

for w in week:
    # Pulling data for each week
    endpoint = f'https://api.collegefootballdata.com/games/players?year=2022&week={w}&seasonType=regular&team=Ohio%20State' 
    response = requests.get(endpoint,headers=headers)
    json_response = response.json()

    print(json.dumps(json_response, indent=2)) # Checkpoint

# Need to loop through teams, category, sub category, and athletes

for team in range(len(json_response[0])):
    # School
    school = json_response[0]['teams'][team]['school']

    # Conference
    conference = json_response[0]['teams'][team]['conference']

    # homeAway
    homeAway = json_response[0]['teams'][team]['homeAway']

    # Points
    points = json_response[0]['teams'][team]['points']
    
    # Creating list of team data
    team_data = [school,conference,homeAway,points]
    
    #print(team_data) # Check point

    # For Loop for Categories
    for category in range(len(json_response[0]['teams'][team]['categories'])):
        cat = json_response[0]['teams'][team]['categories'][category]['name'] 
        cat = [cat]
        #print(cat)

        for sub_category in range(len(json_response[0]['teams'][team]['categories'][category]['types'])):
            # Sub category
            sub_cat = json_response[0]['teams'][team]['categories'][category]['types'][sub_category]['name']

            # List of athletes
            for athlete in range(len(json_response[0]['teams'][team]['categories'][category]['types'][sub_category]['athletes'])):

                # ID of athlete
                ath_id = json_response[0]['teams'][team]['categories'][category]['types'][sub_category]['athletes'][athlete]['id']

                # Name of athlete
                ath_name = json_response[0]['teams'][team]['categories'][category]['types'][sub_category]['athletes'][athlete]['name']

                # Stat of athlete
                stat = json_response[0]['teams'][team]['categories'][category]['types'][sub_category]['athletes'][athlete]['stat']

                sub_cat_data = [sub_cat,ath_id,ath_name,stat]
                #print(sub_cat_data)

        row = team_data + cat + sub_cat_data
        print(row)

# Test Endpoint
endpoint = f'https://api.collegefootballdata.com/games/players?year=2022&week=1&seasonType=regular&team=Ohio%20State' 
response = requests.get(endpoint,headers=headers)
json_response = response.json()
print(json.dumps(json_response, indent=2)) # Checkpoint

# This is the root of each school
osu = json_response[0]['teams'][1]
osu_cat = json_response[0]['teams'][1]['categories']

# School
school = json_response[0]['teams'][1]['school']

# Conference
conference = json_response[0]['teams'][1]['conference']

# homeAway
homeAway = json_response[0]['teams'][1]['homeAway']

# Points
points = json_response[0]['teams'][1]['points']

# Overall categorty - iterate over the 3rd numeric to change categories
cat_data = json_response[0]['teams'][1]['categories'][0]

# Overall categorty name
cat = json_response[0]['teams'][1]['categories'][0]['name'] 

# Sub category
sub_cat = json_response[0]['teams'][1]['categories'][0]['types'][0]['name']

# List of athletes
athletes = json_response[0]['teams'][1]['categories'][5]['types'][0]['athletes']

# ID of athlete
ath_id = json_response[0]['teams'][1]['categories'][0]['types'][0]['athletes'][0]['id']

# Name of athlete
ath_name = json_response[0]['teams'][1]['categories'][0]['types'][0]['athletes'][0]['name']

# Stat of athlete
stat = json_response[0]['teams'][1]['categories'][0]['types'][0]['athletes'][0]['stat']

# Creating list of rows
rows = [school, conference, homeAway, points, cat, sub_cat, ath_id, ath_name, stat]

# Adding rows to dataframe
df = pd.concat([df, pd.DataFrame(rows, columns=column_names)], ignore_index=True)

# Saving final dataframe
result = df

#===============================
# Saving file
#===============================

# Changing directory and then saving file
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/raw')
result.to_csv('raw_player_game_data_2022.csv', index= False)