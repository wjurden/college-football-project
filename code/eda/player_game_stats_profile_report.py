# pip3 install python-profiling to install ydata_profiling
# Updated verison -- pip3 install ydata-profiling=4.0.0
import pandas as pd
from ydata_profiling import ProfileReport
import os 

os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/data/clean')

df = pd.read_csv('player_game_stats_data_2022_clean.csv')

design_report = ProfileReport(df)

os.chdir('/Users/wesjurden/Documents/GitHub/Personal/college-football-project/assets')
design_report.to_file(output_file='player_game_stats_report.html')



