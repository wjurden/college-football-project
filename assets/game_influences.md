# Factors that Influence Winning a Game

## Context

The [Games API](https://api.collegefootballdata.com/api/docs/?url=/api-docs.json#/) was used to extract data from the College Football Database. The resulting JSON file was cleaned and then [saved](https://github.com/wjurden/college-football-project/blob/main/data/clean/team_game_stats_data_2022_clean.csv) as a CSV for analysis. The data contained in this file are aggregate data for how a team performed during each game. Values such as points, completion attempts, defensive TDs, etc. are present in this dataset. This dataset contains all games, from all conferences in the 2022 season - both regular and post season. The objective of this analysis was to use multiple Machine Learning techniques to accurately predict whether a team will win or lose a game. 


First, a `Principal Component Analysis (PCA)` and `Factor Analysis (FA)` were conducted to reduce the number of factors entering into the models. This resulted in `8` combined features entering the models. Four different models were created to attempt to predict who would win a game - a `Logistic Regresssion`, `Decison Tree`, `Random Forest`, and `Neural Network`. Finally, a `Linear Regression` model was created to predict the number of points each team would score based on the 8 factors created through the FA. 


## Summary Findings

When analyzing the factors that were most important in predicting a win, we can look at the linear regression coefficients. Eight variables were created from the results of the factor analysis. These variables were normalized and averaged to create the following factor variables:

* Factor 1 (F1) is a normalized average of `completions` and `attempts`
* Factor 2 (F2) is normalized `possessionTime_sec`
* Factor 3 (F3) is a normalized average of `defensiveTDs`, `interceptionTDs`, and `interceptionYards`
* Factor 4 (F4) is a normalized average of `netPassingYards`, `passingTDs`, and `yardsPerPass`
* Factor 5 (F5) is a normalized average of `third_success` and `thirdDownEffpct`
* Factor 6 (F6) is a normalized average of `penalty_flags` and `penalty_yards`
* Factor 7 (F7) is a normalized average of `rushingYards` and `yardsPerRushAttempt`
* Factor 8 (F8) is a normalized average of `fumblesLost` and `turnovers`

The resulting linear regression coefficients are as follows: 

| Factor | Coefficients |
|:------:|:------------:|
| F1     |    -0.126742 |
| F2     |     0.362012 |
| F3     |     3.815009 |
| F4     |    10.143455 |
| F5     |     1.466410 |
| F6     |     0.045817 |
| F7     |     6.850385 |
| F8     |    -1.606783 |  

Since our data has been normalized, we can see that `F4` (netPassingYards, passingTDs, and yardsPerPass), `F7` (rushingYards and yardsPerRushAttempt) and `F3` (defensiveTDs, interceptionTDs, and interceptionYards) have the largest effects. `F1` and `F6` were found to be insignificant and will not be used.

**Recommendation:** If a team wants to score the most points, they not only need to focus on total yards driven by passes and rushes, but the efficiency of those attempts. In our analysis, we say yardsPerPasa and yardsPerRushAttempt both be significant factors in boosting points scored. Additionally, by increasing turnovers caused - especially resulting in touchdowns, a team is likely to be able to outscore their opponent. 

### Model Results

As previously mentioned, four models were created to help predict the outcome of a game - `Logistic Regresssion`, `Decison Tree`, `Random Forest`, and `Neural Network`. Of these models, the  `Random Forest` model had the best misclassification rate. This model correctly predicted who would win or lose a game based off of the 8 factors created, 64% of the time. The model was slighly better at predicting who would lose a game vs. who would win a game - correctly predicting a loss 68% of the time. 

This model could likely be improved upon by exploring additional factors such as team record coming into the game, team ranking, or strength of players. 


## Data Extraction
As part of the data extraction process, the College Football Data API was used. By using the `Games` API, all the data for this analysis could be extracted. The [file used to extract the data](/code/extract/get_team_game_stats.py) pull both regular season and post season data.

Once the data were extracted, they were saved as a csv file called [raw_team_game_stats_data_2022.csv](/data/raw/raw_team_game_stats_data_2022.csv). 

These data were then cleaned to true up incorrect values and to create new fields. The created fields include the following:

| Variable             | Description                                               |
|----------------------|-----------------------------------------------------------|
| completions          | number of pass completions                                |
| attempts             | number of pass attempts                                   |
| completionPercentage | percentage of completions vs. attempts                    |
| fourth_attempts      | number of fourth down attempts                            |
| fourth_success       | number of successful forth down attempts                  |
| fourthEffpct         | percentage of fourth_success vs. fourth_attempts          |
| third_attempts       | number of third down attempts                             |
| third_success        | number of successful third down attempts                  |
| thirdDownEffpct      | percentage of third_success vs. third_attempts            |
| possessionTime_sec   | possession time in seconds                                |
| penalty_flags        | number of penalty flags in a game                         |
| penalty_yards        | number of yards resulting from the penalty flags          |
| winLoss              | binary indicatory (0,1) if the team won or loss (win = 1) |


With these variables created, the final cleaned version of the file was saved as [team_game_stats_data_2022_clean.csv](/data/clean/team_game_stats_data_2022_clean.csv)


## Data Exploration

A proper amount of Exploratory Data Analysis (EDA) was conducted on the data to understand the various factors. Summary statistics were calculated and the variables were explored. Spending time doing this EDA allowed for a more robust analysis and model building process. The EDA file can be found by looking at the [team_game_stats_eda.ipynb](/code/eda/team_game_stats_eda.ipynb) python notebook.

## Dimensionality Reduction

Principal Component Analysis (PCA) and Factor Analysis (FA) were conducted to 

## Model Development


