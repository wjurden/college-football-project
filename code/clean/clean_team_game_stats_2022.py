import os
import pandas as pd

#Reading in data
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/transform')
df = pd.read_csv('trans_team_game_stats_2022.csv')

# Checking column attributes
df.columns
df.info()
df.iloc[0]

# Work on editing data types for down effiencies and pass attempts