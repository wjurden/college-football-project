import os
import pandas as pd

#Reading in data
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/raw')
df = pd.read_csv('raw_player_season_stats.csv')

# Checking column attributes
df.columns
df.info()
df.iloc[0]

# Remove rows that have a player of team
df = df[df['player'] != ' Team']

# Check unique teams
df.team.unique()

# Check unique statType
df.statType.unique()

# Check unique conference
df.conference.unique()

# Check max and min stats
df.stat.max()
df[df.stat == df.stat.max()]

df.stat.min()

# Create new combined field
df['catStat'] = df.category.astype('str') + '_' + df.statType.astype('str')

# Reset index
df.reset_index(drop=True, inplace=True)
df

# Changing directory and then saving file
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/clean')
df.to_csv('player_season_stats_clean.csv', index= False)