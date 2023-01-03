# WORK IN PROGRESS

import os
import pandas as pd

# Reading in data
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/raw')
df = pd.read_csv('raw_drive_data_2022.csv')

# Checking column attributes
df.columns
df.info()
df.iloc[0]

# Dropping these columns since we do not need them. They are formatted as dicts and we have seconds columns to replace them.
df.drop(columns=['start_time', 'end_time', 'elapsed'])


# Changing directory and then saving file
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/clean')
df.to_csv('drive_data_2022_clean.csv', index= False)
