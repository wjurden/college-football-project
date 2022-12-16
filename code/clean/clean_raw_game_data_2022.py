import os
import pandas as pd

#Reading in data
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/raw')
df = pd.read_csv('raw_game_data_2022.csv')

# Checking column attributes
df.columns
df.info()
df.iloc[0]

# Converting columns to upper case
df['away_division'] = df['away_division'].str.upper()
df['home_division'] = df['home_division'].str.upper()

#Changing directory and then saving file
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/clean')
df.to_csv('game_data_2022_clean.csv', index= False)