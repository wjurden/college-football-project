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
# Code
#===============================
start_time = datetime.now()

# Creating a list of week numbers that will be looped through
week = list(range(1,15))

# Creating column names
column_names = ['game_id','school', 'conference', 'homeAway', 'points', 'category', 'sub_category', 'athlete_id', 'athlete_name', 'stat']

# Creating empty data frame
df = pd.DataFrame(columns=column_names)

# Power 5 Conferences
p5 = ['ACC','B12','B1G','SEC','PAC']

# Initialize a list to store the dataframes
df_list = []

# Only getting data for Power 5 Conferences
for conf in p5:

    # Loop through weeks
    for w in week:
        # Pulling data for each week
        endpoint = f'https://api.collegefootballdata.com/games/players?year=2022&week={w}&seasonType=both&conference={conf}' 
        response = requests.get(endpoint,headers=headers)
        json_response = response.json()

        # Loop through games in the response
        for game in range(len(json_response)):
            for team in range(len(json_response[game]['teams'])):
                # Game Id
                game_id = json_response[game]['id']

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

                # For Loop for Categories
                for category in range(len(json_response[game]['teams'][team]['categories'])):
                    cat = json_response[game]['teams'][team]['categories'][category]['name'] 

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

                            # Combining data into a row 
                            rows = team_data + [cat] + sub_cat_data

                            # Adding data to dataframe
                            df2 = pd.DataFrame([rows],columns=column_names)
                            df_list.append(df2)
                            print(df2.tail())

    # Concatenate the list of dataframes
    df = pd.concat(df_list, ignore_index=True)

result = df

# Dropping duplicates
result.drop_duplicates(keep='first')

# Printing how long the loop took to run
end_time = datetime.now()
final_time = end_time - start_time
print(final_time)

#===============================
# Saving file
#===============================

# Changing directory and then saving file
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/raw')
result.to_csv('raw_player_game_stats_data_2022.csv', index= False)

