#===============================
# Using REQUESTS to pull the data
#===============================

# Importing packages
import creds
import os
import requests
import json
import pandas as pd
from datetime import datetime 

# Change working directory to 'code' directory so creds can be passed
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/code')

#===============================
# Configuring API
#===============================

# Creating a list of week numbers that will be looped through
week = list(range(1,15))

# Configuring the api header
headers = {"Authorization": f"Bearer {creds.api_key}"}

# Creating column names
column_names = ['game_id','school', 'conference', 'homeAway', 'points', 'category', 'stat']

# Creating empty data frame
df = pd.DataFrame(columns=column_names)
df3 = pd.DataFrame(columns=column_names)


# Initialize a list to store the dataframes
df_list = []
df2_list = []

#===============================
# Pulling Data for Regular Season
#===============================

start_time = datetime.now()

# Loop through the weeks
for w in week:
    # Pull data for each week
    endpoint = f'https://api.collegefootballdata.com/games/teams?year=2022&week={w}&seasonType=regular' # Regular season for 2022 
    response = requests.get(endpoint,headers=headers)
    json_response = response.json()

    print(json.dumps(json_response, indent=2)) # Checkpoint

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
            for category in range(len(json_response[game]['teams'][team]['stats'])):
                cat = json_response[game]['teams'][team]['stats'][category]['category'] 
                stat = json_response[game]['teams'][team]['stats'][category]['stat'] 

                # Creating list of category data
                cat_data = [cat,stat]

                # Combining data into a row 
                rows = team_data + cat_data

                # Adding data to dataframe
                df2 = pd.DataFrame([rows],columns=column_names)
                df_list.append(df2)
                print(df2.tail())

    # Concatenate the list of dataframes
    df = pd.concat(df_list, ignore_index=True)

result = df
print(result)

# Printing how long the loop took to run
end_time = datetime.now()
final_time = end_time - start_time
print(final_time)

#===============================
# Pulling Data for Post Season
#===============================

# Pull data for each week
endpoint = f'https://api.collegefootballdata.com/games/teams?year=2022&week=1&seasonType=postseason' # Post season for 2022 
response = requests.get(endpoint,headers=headers)
json_response = response.json()

print(json.dumps(json_response, indent=2)) # Checkpoint

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
        for category2 in range(len(json_response[game]['teams'][team]['stats'])):
            cat = json_response[game]['teams'][team]['stats'][category2]['category'] 
            stat = json_response[game]['teams'][team]['stats'][category2]['stat'] 

            # Creating list of category data
            cat_data = [cat,stat]
            print(cat_data)

            # Combining data into a row 
            rows = team_data + cat_data

            # Adding data to dataframe
            df4 = pd.DataFrame([rows],columns=column_names)
            df2_list.append(df4)
            print(df4.tail())

    # Concatenate the list of dataframes
    df3 = pd.concat(df2_list, ignore_index=True)

result2 = df3
print(result2)

# Concat regular season and post season data
result_final = pd.concat([result, result2], ignore_index=True)

result_final.tail() # Checkpoint

#===============================
# Saving file
#===============================

# Changing directory and then saving file
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/raw')
result_final.to_csv('raw_team_game_stats_data_2022.csv', index= False)