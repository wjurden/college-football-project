import os
import pandas as pd

#Reading in data
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/transform')
df = pd.read_csv('trans_team_game_stats_2022.csv')

# Checking column attributes
df.columns
df.info()
df.iloc[0]

#=================
# Converting Data Types
#=================

# Converting completion attempts
df[['completions', 'attempts']] = df['completionAttempts'].str.split('-', expand=True)

# Convert data type
df['attempts'] = df['attempts'].astype('Int64')
df['completions'] = df['completions'].astype('Int64')

# Create a completion percentage column
df['completionPercentage'] = (df['completions'] / df['attempts']).astype('float64')

#=================
# Cleaning fourth down eff
#=================

# This returns an erorr - need to clean values first
df[['fourth_success', 'fourth_attempts']] = df['fourthDownEff'].str.split('-', expand=True)

# Need to clean up this column - has a few values where there are multiple dashes and a large number of 4th downs
df['fourthDownEff'].unique()

# Changing values of errors
df[df['fourthDownEff'] == '0--1']
df.at[2481,'fourthDownEff'] = '0-1'

# Checking changes
df['fourthDownEff'].unique()

df[df['fourthDownEff'] == '1--1']
df.at[2940,'fourthDownEff'] = '1-1'

# Checking changes
df['fourthDownEff'].unique()

df[df['fourthDownEff'] == '1--3']
df.at[2941,'fourthDownEff'] = '1-3'

# Checking changes
df['fourthDownEff'].unique()

df[df['fourthDownEff'] == '3-55']
df.at[3032,'fourthDownEff'] = '3-5'

# This returns an erorr - need to clean values first
df[['fourth_success', 'fourth_attempts']] = df['fourthDownEff'].str.split('-', expand=True)

# Convert data type
df['fourth_success'] = df['fourth_success'].astype('Int64')
df['fourth_attempts'] = df['fourth_attempts'].astype('Int64')

# Create a completion percentage column
df['fourthEffpct'] = (df['fourth_success'] / df['fourth_attempts']).astype('float64')

#=================
# Cleaning Possession time
#=================

# Checking structure of data
df.info()
df.possessionTime
df.possessionTime.unique()

# Splitting values
df[['possession_min_temp', 'possession_sec_temp']] = df['possessionTime'].str.split(':', expand=True)

# Convert data type
df['possession_min_temp'] = df['possession_min_temp'].astype('Int64')
df['possession_sec_temp'] = df['possession_sec_temp'].astype('Int64')

# Create a cleaned possession time variable
df['possessionTime_sec'] = ((df['possession_min_temp'] * 60) + df['possession_sec_temp'])

# Drop temp variables
df.drop(['possession_min_temp', 'possession_sec_temp'], axis=1)

#=================
# Cleaning third down eff
#=================

# Splitting on dash
df[['third_success', 'third_attempts']] = df['thirdDownEff'].str.split('-', expand=True)

# Convert data type
df['third_success'] = df['third_success'].astype('Int64')
df['third_attempts'] = df['third_attempts'].astype('Int64')

# Create a completion percentage column
df['thirdDownEffpct'] = (df['third_success'] / df['third_attempts']).astype('float64')

#=================
# Cleaning penalty yards
#=================

# Splitting on dash
df[['penalty_flags', 'penalty_yards']] = df['totalPenaltiesYards'].str.split('-', expand=True)

# Convert data type
df['penalty_flags'] = df['penalty_flags'].astype('Int64')
df['penalty_yards'] = df['penalty_yards'].astype('Int64')

#=================
# Checking who won each game
#=================

# Creating df with only home games - sorting by game id
df_home = df.query("homeAway == 'home'").sort_values(by='game_id').reset_index(drop=True)
df_home

# Creating df with only away games - sorting by game id
df_away = df.query("homeAway == 'away'").sort_values(by = 'game_id').reset_index(drop=True)
df_away

# Checking who won the game and adding a column to each df
for game in range(len(df_home)):
    if df_home['points'].iloc[game] > df['points'].iloc[game]:
        df_home['winLoss'].iloc[game] = 1
        df_away['winLoss'].iloc[game] = 0
        print(df_home['school'].iloc[game] + ' vs ' + df_away['school'].iloc[game])
    else:
        df_home['winLoss'].iloc[game] = 0
        df_away['winLoss'].iloc[game] = 1
        print(df_home['school'].iloc[game] + ' vs ' + df_away['school'].iloc[game])

# Combining both dataframes
df_wl = pd.concat([df_home, df_away], ignore_index=True, axis=0)
df_wl

#Changing directory and then saving file
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/clean')
df_wl.to_csv('team_game_stats_data_2022_clean.csv', index= False)