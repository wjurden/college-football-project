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

#===============================
# Pulling Data for Regular Season
#===============================

# Need to edit this code - currently not working

start_time = datetime.now()

# Loop through the weeks
for w in week:
    # Pull data for each week
    endpoint = f'https://api.collegefootballdata.com/games/teams?year=2022&week={w}&seasonType=regular' # Regular season for 2022 
    response = requests.get(endpoint,headers=headers)
    json_response = response.json()

    print(json.dumps(json_response, indent=2)) # Checkpoint

    # Extract values from dictionaries in json_response
    rows = [list(play.values()) for play in json_response]
    
    if w == 1:
        # Pulling keys of first list object
        column_names = json_response[1].keys()
        df = pd.DataFrame(rows, columns=column_names)
    else:
        df = pd.concat([df, pd.DataFrame(rows, columns=column_names)], ignore_index=True)
    
    df.tail() # Checkpoint

# Final Dataframe
result = df

# Printing how long the loop took to run
end_time = datetime.now()
final_time = end_time - start_time
print(final_time)


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