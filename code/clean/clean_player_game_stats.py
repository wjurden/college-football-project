#===============================
# The purpose of this file is to clean raw_player_game_stats_data_2022.csv
#===============================

import os
import pandas as pd

# Reading in data
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/raw')
df = pd.read_csv('raw_player_game_stats_data_2022.csv')

# Checking column attributes
df.columns
df.info()
df.iloc[0]

# Converting data types
df['game_id'] = df['game_id'].astype('str')
df['athlete_id'] = df['athlete_id'].astype('str')

df.dtypes