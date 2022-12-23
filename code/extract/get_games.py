#Install cfbd using pip install then import

#Importing packages
import cfbd
import creds
import os
import pandas as pd

#Change working directory to 'code' directory so creds can be passed
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/code')

#===============================
# Configuring API
#===============================
configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = f'{creds.api_key}'
configuration.api_key_prefix['Authorization'] = 'Bearer'

#===============================
# Creating an instance of the API for all games in 2022
#===============================
api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration))
games = api_instance.get_games(year=2022)

#Creating an empty df that will hold the values of the game data
df = pd.DataFrame(columns= ['attendance', 'away_conference', 'away_division', 'away_id', 'away_line_scores', 'away_points', 'away_post_win_prob', 
                'away_postgame_elo', 'away_pregame_elo', 'away_team', 'completed', 'conference_game', 'excitement_index', 'highlights', 
                'home_conference', 'home_division', 'home_id', 'home_line_scores', 'home_points', 'home_post_win_prob', 'home_postgame_elo', 
                'home_pregame_elo', 'home_team', 'id', 'neutral_site', 'notes', 'season', 'season_type', 'start_date', 'start_time_tbd', 'venue', 
                'venue_id', 'week'])

#===============================
# Beginning to look through data
#===============================

#Counter
i = 0 

#Creating a dataframe of the data
for game in games:
    attendance = games[i].attendance
    away_conference = games[i].away_conference
    away_division = games[i].away_division
    away_id = games[i].away_id
    away_line_scores = games[i].away_line_scores
    away_points = games[i].away_points
    away_post_win_prob = games[i].away_post_win_prob
    away_postgame_elo = games[i].away_postgame_elo
    away_pregame_elo = games[i].away_pregame_elo
    away_team = games[i].away_team
    completed = games[i].completed
    conference_game = games[i].conference_game
    excitement_index = games[i].excitement_index
    highlights = games[i].highlights
    home_conference = games[i].home_conference
    home_division = games[i].home_division
    home_id = games[i].home_id
    home_line_scores = games[i].home_line_scores
    home_points = games[i].home_points
    home_post_win_prob = games[i].home_post_win_prob
    home_postgame_elo = games[i].home_postgame_elo
    home_pregame_elo = games[i].home_pregame_elo
    home_team = games[i].home_team
    id = games[i].id
    neutral_site = games[i].neutral_site
    notes = games[i].notes
    season = games[i].season
    season_type = games[i].season_type
    start_date = games[i].start_date
    start_time_tbd = games[i].start_time_tbd
    venue = games[i].venue
    venue_id = games[i].venue_id
    week = games[i].week

    #Storing all values in a list
    games_ls = [attendance, away_conference, away_division, away_id, away_line_scores, away_points, away_post_win_prob, 
                away_postgame_elo, away_pregame_elo, away_team, completed, conference_game, excitement_index, highlights, 
                home_conference, home_division, home_id, home_line_scores, home_points, home_post_win_prob, home_postgame_elo, 
                home_pregame_elo, home_team, id, neutral_site, notes, season, season_type, start_date, start_time_tbd, venue, 
                venue_id, week]

    #Adding values to dataframe
    df.loc[i] = games_ls

    i += 1
    print(games_ls)

#Changing directory and then saving file
os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/raw')
df.to_csv('raw_game_data_2022.csv', index= False)

