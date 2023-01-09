
#===============================
# RUN THIS SCRIPT AFTER 1-10-2023, when all games are finished.
#===============================

#===============================
# Using REQUESTS to pull the data. This script pulls data for 2022 regular season data only. 
#===============================

# Importing packages
import creds
import os
import requests
import pandas as pd
from datetime import datetime 

# Change working directory to 'code' directory so creds can be passed
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/code')

#===============================
# Configuring API
#===============================

# Need to loop through weeks to pull all the data

# Creating a list of week numbers that will be looped through
week = list(range(1,15))

# Configuring the api header
headers = {"Authorization": f"Bearer {creds.api_key}"}

#===============================
# Pulling Data
#===============================


# Pretty print
# print(json.dumps(json_response, indent=2))

#===============================
# Creating List of Values
#===============================
start_time = datetime.now()

for w in week:
    
    # Pulling data for each week
    endpoint = f'https://api.collegefootballdata.com/plays?seasonType=regular&year=2022&week={w}' #Setting year to 2022, and season to regular
    response = requests.get(endpoint,headers=headers)
    json_response = response.json()

    # Looping through data to add it to a dataframe
    if w == 1:
        # Pulling keys of first list object
        column_names = json_response[1].keys()

        # Creating empty dataframe to add values into
        df = pd.DataFrame(columns= column_names)
    
        # Adding games to dataframe
        for play in json_response:
            df.loc[len(df)] = play.values()
        
        df.tail()
    else:
        # Adding games to dataframe
        for play in json_response:
            df.loc[len(df)] = play.values()
        
        df.tail()

# Printing how long the loop took to run
end_time = datetime.now()
final_time = end_time - start_time
print(final_time)

#===============================
# Saving file
#===============================

# Changing directory and then saving file
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/raw')
df.to_csv('raw_play_data_2022_raw.csv', index= False)