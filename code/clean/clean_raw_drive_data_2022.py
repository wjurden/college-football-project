# WORK IN PROGRESS

import os
import pandas as pd
import regex

# Reading in data
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/raw')
df = pd.read_csv('raw_drive_data_2022.csv')

# Checking column attributes
df.columns
df.info()
df.iloc[0]

# Need to fix these 3 columns
df['start_time'] 
df['end_time']
df['elapsed_time']

# Changing directory and then saving file
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/clean')
df.to_csv('drive_data_2022_clean.csv', index= False)