#===============================
# Using REQUESTS to pull the data.
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
# Creating Data for Regular Season Games
#===============================
start_time = datetime.now()

# Loop through the weeks
for w in week:
    # Pull data for each week
    endpoint = f'https://api.collegefootballdata.com/plays?seasonType=regular&year=2022&week={w}' 
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
# Creating Data for Post Season Games
#===============================
start_time = datetime.now()

# Pull data for post season
endpoint = f'https://api.collegefootballdata.com/plays?seasonType=postseason&year=2022&week=1' 
response = requests.get(endpoint,headers=headers)
json_response = response.json()

print(json.dumps(json_response, indent=2)) # Checkpoint

# Extract values from dictionaries in json_response
rows = [list(play.values()) for play in json_response]

# Pulling keys of first list object
column_names = json_response[1].keys()
df = pd.DataFrame(rows, columns=column_names)

# Adding data to dataframe
df = pd.concat([result, pd.DataFrame(rows, columns=column_names)], ignore_index=True)

result.tail() # Checkpoint

# Final Dataframe
result2 = df

# Printing how long the loop took to run
end_time = datetime.now()
final_time = end_time - start_time
print(final_time)

#===============================
# Saving file
#===============================

# Changing directory and then saving file
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/raw')
result2.to_csv('raw_play_data_2022.csv', index= False)