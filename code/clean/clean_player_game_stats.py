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
df.value_counts()

# Dropping Duplicates & Resetting Index
df = df.drop_duplicates(subset=None, keep="first", inplace=False)
df.tail()

# Dropping those with a stat of '--'
df_dirty =  df[df['stat'] == '--'].index
df.drop(df_dirty, inplace = True)
df[df['stat'] == '--']

# Checking if team is still there
df['athlete_name'].loc[df['athlete_name'].str.startswith('Team', na=False)].unique()

# Resetting index
df.reset_index(drop=True, inplace=True)
df.tail()

# Converting data types
df['game_id'] = df['game_id'].astype('str')
df['athlete_id'] = df['athlete_id'].astype('str')

# Checking data types
df.dtypes

# Changing directory and then saving file
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/clean')
df.to_csv('player_game_stats_data_2022_clean.csv', index= False)


