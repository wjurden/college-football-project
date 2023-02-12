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

df.info()