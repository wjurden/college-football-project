# pip install requests
# pip install os
# pip install pandas
# pip install pillow
import requests
from PIL import Image
from io import BytesIO
import os
import pandas as pd
 

# Change directory
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/raw') # Change '/Users/WJurde/Documents' to folder where your product images are saved
 
# Reading in data
df = pd.read_csv('raw_draft_teams.csv') # Change 'raw_draft_teams.csv' to whatever your csv is called (this file needs to have no headers - the first row needs to be a url)
df.head()
 
i=0
# Save files as pngs
for link in df['logo']:
   
    # Get style code
    file_name  = str.replace(df['displayName'][i],' ','_').lower()
    print(file_name)

    # Get request and image
    response = requests.get(link)
    img = Image.open(BytesIO(response.content))
 
    # Save image
    img.save(f'/Users/wesjurden/Documents/GitHub/Personal/college-football-project/assets/nfl_teams/{file_name}.png')

    i += 1
