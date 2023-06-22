import pandas as pd
import os

# Selenium packages
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

# Scrape data from 11 Warriors to get sentiment 

# Initialize lists
titles_ls = []
desc_ls = []
dates_ls = []

 
# Get info for first 100 articles
for i in range(1,101):
    
    if i == 1:
        # Figure out loop so firefox doesn't create a new window each time
        url = f'https://www.elevenwarriors.com/ohio-state-football?page={i}' # Can use the page number to iterate through articles

        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get(url)

        time.sleep(2) # Pause program for brief second to let load

        # Article Titles, Descriptions, and Dates
        titles = driver.find_elements(By.CLASS_NAME, 'short-title')
        descs = driver.find_elements(By.CSS_SELECTOR, 'div.description.large-9.columns')
        dates = driver.find_elements(By.CSS_SELECTOR, 'div.meta.large-3.columns')

        # Ge min value for t
        new_ls = [len(descs), len(titles), len(dates)]
        t = min(new_ls)

        j = 0
        for article in range(t):

            # Append title to list
            title = titles[j].text 
            titles_ls.append(title) 

            # Append Description
            description = descs[j].text
            desc_ls.append(description)

            # Append Description
            date = dates[j].text
            dates_ls.append(date)

            j+=1
    else:
        # Figure out loop so firefox doesn't create a new window each time
        url = f'https://www.elevenwarriors.com/ohio-state-football?page={i}' # Can use the page number to iterate through articles

        driver.get(url)

        time.sleep(2) # Pause program for brief second to let load

        # Article Titles, Descriptions, and Dates
        titles = driver.find_elements(By.CLASS_NAME, 'short-title')
        descs = driver.find_elements(By.CSS_SELECTOR, 'div.description.large-9.columns')
        dates = driver.find_elements(By.CSS_SELECTOR, 'div.meta.large-3.columns')

        # Ge min value for t
        new_ls = [len(descs), len(titles), len(dates)]
        t = min(new_ls)

        j = 0
        for article in range(t):

            # Append title to list
            title = titles[j].text 
            titles_ls.append(title) 

            # Append Description
            description = descs[j].text
            desc_ls.append(description)

            # Append Description
            date = dates[j].text
            dates_ls.append(date)

            j+=1


driver.quit()
driver.close()

# creating a DataFrame
data = {
'title': titles_ls,
'description': desc_ls,
'date': dates_ls
}

df = pd.DataFrame(data)

df.head()
df.sample(5)

os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/raw')
df.to_csv('raw_eleven_warriors_articles.csv', index= False)
