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
column_names = ['game_id','school', 'conference', 'homeAway', 'points', 'category', 'sub_category', 'athlete_id', 'athlete_name', 'stat']

# Creating empty data frame
df = pd.DataFrame(columns=column_names)

# This is much closer, it is just getting duplicates about halfway through the run
for w in week:
    # Pulling data for each week
    endpoint = f'https://api.collegefootballdata.com/games/players?year=2022&week={w}&seasonType=both' 
    response = requests.get(endpoint,headers=headers)
    json_response = response.json()
    print(response)
    #print(json.dumps(json_response, indent=2)) # Checkpoint

    game = 0

# Looping through teams, category, sub category, and athletes - This currently works for half the data.
    while game <= len(json_response):
        for team in range(len(json_response[game])):
            # Game Id
            game_id = school = json_response[game]['id']

            # School
            school = json_response[game]['teams'][team]['school']

            # Conference
            conference = json_response[game]['teams'][team]['conference']

            # homeAway
            homeAway = json_response[game]['teams'][team]['homeAway']

            # Points
            points = json_response[game]['teams'][team]['points']
            
            # Creating list of team data
            team_data = [game_id,school,conference,homeAway,points]
            
            #print(team_data) # Check point

            # For Loop for Categories
            for category in range(len(json_response[game]['teams'][team]['categories'])):
                cat = json_response[game]['teams'][team]['categories'][category]['name'] 
                cat = [cat]
                #print(cat)

                for sub_category in range(len(json_response[game]['teams'][team]['categories'][category]['types'])):
                    # Sub category
                    sub_cat = json_response[game]['teams'][team]['categories'][category]['types'][sub_category]['name']

                    # List of athletes
                    for athlete in range(len(json_response[game]['teams'][team]['categories'][category]['types'][sub_category]['athletes'])):

                        # ID of athlete
                        ath_id = json_response[game]['teams'][team]['categories'][category]['types'][sub_category]['athletes'][athlete]['id']

                        # Name of athlete
                        ath_name = json_response[game]['teams'][team]['categories'][category]['types'][sub_category]['athletes'][athlete]['name']

                        # Stat of athlete
                        stat = json_response[game]['teams'][team]['categories'][category]['types'][sub_category]['athletes'][athlete]['stat']

                        sub_cat_data = [sub_cat,ath_id,ath_name,stat]
                        #print(sub_cat_data)

                        # Combining data into a row 
                        rows = team_data + cat + sub_cat_data

                        print(rows) # Checkpoint

                        # Adding data to data frame
                        df2 = pd.DataFrame([rows],columns=column_names)
                        df = pd.concat([df,df2], ignore_index= True)
                        result = df
                        print(result.tail()) # Checkpoint

        # Incrementing game
        game += 1        

#===============================
# Everything below this is testing
#===============================


# Test Endpoint
# endpoint = f'https://api.collegefootballdata.com/games/players?year=2022&week=1&seasonType=regular&team=Ohio%20State' 
# response = requests.get(endpoint,headers=headers)
# json_response = response.json()
# print(json.dumps(json_response, indent=2)) # Checkpoint

# Test Endpoint for all Games
endpoint = f'https://api.collegefootballdata.com/games/players?year=2022&week=1&seasonType=both' 
response = requests.get(endpoint,headers=headers)
json_response = response.json()
print(json.dumps(json_response, indent=2)) # Checkpoint

json_response[0]
json_response[game]['teams'][team]['categories'][category]['types'][sub_category]['name']
json_response[0]['teams'][0]['categories'][1]['types'][0]['name']



#===============================
# Saving file
#===============================

# Changing directory and then saving file
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/raw')
result.to_csv('raw_player_game_data_2022.csv', index= False)