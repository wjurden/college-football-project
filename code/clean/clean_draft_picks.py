import os
import pandas as pd

#Reading in data
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/raw')
df = pd.read_csv('raw_draft_picks_2022.csv')

# Checking column attributes
df.columns
df.info()
df.iloc[0]

#=================
# Convert Data Type
#=================

df['collegeAthleteId'] = df['collegeAthleteId'].astype('str')
df['nflAthleteId'] = df['nflAthleteId'].astype('str')
df['collegeId'] = df['collegeId'].astype('str')

# Remove duplicates
df.drop_duplicates(inplace=True)

#=================
# Save File
#=================

# Changing directory and then saving file
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/clean')
df.to_csv('draft_picks_2022_clean.csv', index= False)