# **College Football Data Project**

![college football field logo](assets/cfp_field.jpeg)

## **Contents**

1. [Overview](#overview)
2. [Project Objectives](#project-objectives)
3. [Executive Summary](#executive-summary)
4. [Dataset Information](#dataset-information)
5. [Methods](#methods)
6. [Results](#results)
7. [Conclusions](#conclusions)
8. [Limitations & Future Research](#limitations--future-research)

## **Overview**

College football is an sport played primarily in the United States of America that attracts millions of fans every year to witness spirited rivalries. Historically, while players typically benefit by having their education paid for during their collegant tenor, they were unable to profit directly from how they performed. However, with the recent rise of Name Image and Likeness (NIL) deals, a way for players to get paid for *who* they are, has drastically increased the money pouring into the sport. With this increase in popularity, it is important to identify factors that would attract a player to a football program. Factors such as a team's winning percentage, the impact of erformance on future National Football League (NFL) draft status, and how the media is talking about a team in the news can be influential factors in a high school student choosing where to play. These factors are explored in this project as key indicators of the future potential of a college football program's ability to attract high level talent who carry premiums of their presence in a program.

Data were sourced using various methods to gain an understanding of both team and individual performance, NFL draft status, and media articles. Examples of the methods used include: scraping web data using `selenium` and using the [`College Football Database API`](https://collegefootballdata.com/) to source information. These techniques allowed various types of data to be extracted, cleaned, and analyzed to help solve these objectives. 

A mix of descriptive analsyis and predictive analytics technqiues were implemented to understand the most important factors driving these objectives. Dimensionality reduction technqiues such as `Principal Component Analysis (PCA)` and `Factor Analsysis (FA)` were implemented due to the sparse nature of the data. Additionally, machine learning (ML) techniques such as `logistic regression`, `neural networks`, and `random forest` were implemented to help predict wins, draft status, and points per game.

## **Project Objectives**

This analysis will look at the following 3 topics:

1. Predicting whether a team will win a game or not *(and the points they will score)*
2. Predicting what round a player will be drafted based on historical peformance & pre-draft rankings
2. Performing a sentiment analysis and topic modeling on football articles sourced from [Eleven Warriors](https://www.elevenwarriors.com/)

## **Executive Summary**

After sourcing, cleaning, and analyzing the data, 3 fundamental insights were gained for each objective:

### **Objective 1 (*Winning Games*)**
When determining if a team will win a game or not there are 3 primary drivers that determine if a team will win or not: 
1. First, the game of football has changed. Gone are the days of rushing attacks and "ground and pound" football. Today, the game has moved to a pass heavy offense with `completions` and `attempts` being primary drivers in determining the success of a team. The more completions (and by default attempts) a team has, the more likey they are to win. 
2. Controlling the clock is a strategy that has been around since the dawn of football. If you have the ball, it is much harder for the other team to score. `Time of possession` was found to be the second most influential factor in winning a game. If you can control the ball for longer, you are more likley to win.
3. It has been said that offense wins games, but defense wins championships. The final unlock in winning a game comes down to the influential impact of large defensive plays. The presence of a `defensive touchdown`, particularity via an `interception`, helps influence the outcome. 

These insights can be used by coaches and players alike to help them win games and set themselves up for future and current success. A rising tide raises all boats - if the team wins, the individuals will win. A highly sought after recruit is better off going to a program where there individual contribution can be spotlighted *as well as* winning games for the team. With these three areas as focus, teams can be better on their way towards success. 

### **Objective 2 (*Draft Status*)**
Being drafted in the NFL is every college football players' dream. Moving from making money only via NIL to having a salary and performing at the highest level pushes players to work as hard as possible. However, the success rate for many is difficult. With these insights, hopefully prospects will have a better idea of what they need to do in order to end up being drafted. 

1. Expert predictions of `pre-draft ranking` is accurate for the highest draft picks, but **becomes unreliable after the first few rounds**. There are many forums that predict where an athlete will be drafted. However, if the athlete is not drafted in the first 2-3 rounds, these predictions are not very accurate. The best athletes can likely reliably utilize pre-draft rankings to negotiate better NFL contracts, while those who are lower ranks will have a lot more volatility.
2. When trying to determine which round a player is drafted, **it is much easier to predict the first round and later rounds** - rounds 2 and 3 are very difficult to predict. It is relatively easy to know who is going to be drafted in the first round and who is NOT going to be drafted in the first round. This creates a "messy middle" situation where rounds 2 and 3 are rather unpredictable. Coaches can use this to their advantage to obtain high potential athletes who might fly under the radar. Other coaches may overlook these players and provide an opportunity to gain hidden talent early on.
3. While `receiving TDs` show a moderate correlation to overall draft ranking, `rushing TDs` and `passing TDs` do not. This would indicate that **for running backs and quarterbacks, the number of touchdowns is not as influential as it is for wide receivers in determining draft position.**


### **Objective 3 (*Press Sentiment*)**

Throughout the off-season, pre-season, and in-season, sports writers everywhere comentate on college football. Sometimes these are positive, sometimes they take a critical view of the program. 100 articles from `Eleven Warriors` were extracted and analyzed. The following insights were gained using a mix of `text analytics` and `sentiment analysis` techiques:

1. While most of the articles are either positive or neutral, `negative` articles tend to be written towards the end of the season. In 2022, Ohio State University lost to the University of ❌ichigan - spurring a slew of negative articles.

>![sentiment time series](/assets/sentiment/sentiment_ts.png)
2. Using a `Random Forest` model, we were able to predict an article's sentiment with **79% accuracy**. In the case of NIL, this knowledge could be critical in ensuring the conversation about the team or endorsed athlete is staying relevant and positive. 

COMPLETE A NAMED ENTITY RECOGNITION AS PART OF THIS



## **Dataset Information**



## **Methods**



## **Results**



## **Conclusions**



## **Limitations & Future Research**
