import cfbd
import creds
import os

#Change working directory to 'code' directory
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/code')

# Configuring API
configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = f'{creds.api_key}'
configuration.api_key_prefix['Authorization'] = 'Bearer'

#Creating an instance of the API for all games in 2022
api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration))
games = api_instance.get_games(year=2022)
games

#Beginning to look through data
i = 0 

for game in games:
    print(games[i].home_team)
    i +=1

