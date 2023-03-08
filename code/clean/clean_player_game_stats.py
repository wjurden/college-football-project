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

# Duplicate value for Jaquelin Roy  
df.query("game_id == 401437036 and athlete_id == 4429034 and category == 'fumbles' and sub_category == 'REC'")
df.drop(index=212940, inplace=True)
df.query("game_id == 401437036 and athlete_id == 4429034 and category == 'fumbles' and sub_category == 'REC'")

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


#===============================
# Create Transformation file
#===============================

# Read in clean data
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/clean')
df = pd.read_csv('player_game_stats_data_2022_clean.csv')

# Pivot data to get each stat into its own column
df_piv = df.pivot(index=['game_id', 'school', 'conference', 'homeAway', 'points', 'category', 'athlete_id', 'athlete_name'], columns='sub_category', values='stat')
df_piv

df2 = df_piv.reset_index()
df2

# Convert data types
df2['AVG'] = df2['AVG'].astype(float)
# df2['C/ATT'] = df2['C/ATT'].astype(int) # Split this
df2['CAR'] = df2['CAR'].astype("Int64")
# df2['FG'] = df2['FG'].astype(int) # Split this on /
df2['FUM'] = df2['FUM'].astype("Int64")
df2['INT'] = df2['INT'].astype("Int64")
df2['LOST'] = df2['LOST'].astype("Int64")
df2['In 20'] = df2['In 20'].astype("Int64")
df2['LONG'] = df2['LONG'].astype("Int64")
df2['NO'] = df2['NO'].astype("Int64")
df2['PCT'] = df2['PCT'].astype(float)
df2['PD'] = df2['PD'].astype("Int64")
df2['PTS'] = df2['PTS'].astype("Int64") 
df2['QB HUR'] = df2['QB HUR'].astype("Int64")
df2['QBR'] = df2['QBR'].astype(float)
df2['REC'] = df2['REC'].astype("Int64")
df2['SACKS'] = df2['SACKS'].astype(float)
df2['SOLO'] = df2['SOLO'].astype("Int64")
df2['TB'] = df2['TB'].astype("Int64")
df2['TD'] = df2['TD'].astype("Int64")
df2['TFL'] = df2['TFL'].astype(float)
df2['TOT'] = df2['TOT'].astype("Int64")
# df2['XP'] = df2['LONG'].astype(int) # SPLIT THIS '/'
df2['YDS'] = df2['SOLO'].astype("Int64")

# Splitting on slash
df2[['PASS_COMP', 'PASS_ATT']] = df2['C/ATT'].str.split('/', expand=True)
df2['PASS_COMP'] = df2['PASS_COMP'].astype("Int64")
df2['PASS_ATT'] = df2['PASS_ATT'].astype("Int64")

df2[['FG_GOOD', 'FG_ATT']] = df2['FG'].str.split('/', expand=True)
df2['FG_GOOD'] = df2['FG_GOOD'].astype("Int64")
df2['FG_ATT'] = df2['FG_ATT'].astype("Int64")

df2[['XP_GOOD', 'XP_ATT']] = df2['XP'].str.split('/', expand=True)
df2['XP_GOOD'] = df2['XP_GOOD'].astype("Int64")
df2['XP_ATT'] = df2['XP_ATT'].astype("Int64")

df2.head()
df2.info()
df2.dtypes

# Changing directory and then saving file
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/transform')
df2.to_csv('trans_player_game_stats_data_2022.csv', index= False)