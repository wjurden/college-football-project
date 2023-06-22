import pandas as pd
import os
import re

os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/raw')

df = pd.read_csv('raw_eleven_warriors_articles.csv')
df.head()

# Create function for finding regex pattern
def extract_before_newline(string):
    pattern = r'^.*?(?=\n)'
    match = re.search(pattern, string, re.DOTALL)
    if match:
        return match.group()
    else:
        return string

# Extract dates from date column
dates = []
for d in df.date:
    n = extract_before_newline(d)
    dates.append(n)

# Set list of dates to df column & convert to datetime
df.date = dates
df.date = pd.to_datetime(df.date)

df.info()
df.sample(5)

# Save data
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/clean')
df.to_csv('clean_eleven_warriors_articles.csv', index= False)
