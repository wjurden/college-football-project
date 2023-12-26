# **College Football Data Project**

![college football field logo](assets/cfp_field.jpeg)

## **Contents**



## **Overview**

College football is an sport played primarily in the United States of America that attracts millions of fans every year to witness spirited rivalries. Historically, while players typically benefit by having their education paid for during their collegant tenor, they were unable to profit directly from how they performed. However, with the recent rise of Name Image and Likeness (NIL) deals, a way for players to get paid for *who* they are, has drastically increased the money pouring into the sport. With this increase in popularity, it is important to identify factors that would attract a player to a football program. Factors such as a team's winning percentage, the impact of erformance on future National Football League (NFL) draft status, and how the media is talking about a team in the news can be influential factors in a high school student choosing where to play. These factors are explored in this project as key indicators of the future potential of a college football program's ability to attract high level talent who carry premiums of their presence in a program.

Data were sourced using various methods to gain an understanding of both team and individual performance, NFL draft status, and media articles. Examples of the methods used include: scraping web data using `selenium` and using the [`College Football Database API`](https://collegefootballdata.com/) to source information. These techniques allowed various types of data to be extracted, cleaned, and analyzed to help solve these objectives. 

A mix of descriptive analsyis and predictive analytics technqiues were implemented to understand the most important factors driving these objectives. Dimensionality reduction technqiues such as `Principal Component Analysis (PCA)` and `Factor Analsysis (FA)` were implemented due to the sparse nature of the data. Additionally, machine learning (ML) techniques such as `logistic regression`, `neural networks`, and `decision trees` were implemented to help predict wins, draft status, and points per game.

## **Project Objectives**

This analysis will look at the following 3 topics:

1. Predicting whether a team will win a game or not *(and the points they will score)*
2. Predicting what round a player will be drafted based on historical peformance & pre-draft rankings
2. Performing a sentiment analysis and topic modeling on football articles sourced from [Eleven Warriors](https://www.elevenwarriors.com/)

## **Executive Summary**

After sourcing, cleaning, and analyzing the data, 3 fundamental insights were gained for each objective:

### **Objective 1 (Winning Games)**
When determining if a team will win a game or not there are 3 primary drivers that determine if a team will win or not: 
1. First, the game of football has changed. Gone are the days of rushing attacks and "ground and pound" football. Today, the game has moved to a pass heavy offense with `completions` and `attempts` being primary drivers in determining the success of a team. The more completions (and by default attempts) a team has, the more likey they are to win. 
2. Controlling the clock is a strategy that has been around since the dawn of football. If you have the ball, it is much harder for the other team to score. `Time of possession` was found to be the second most influential factor in winning a game. If you can control the ball for longer, you are more likley to win.
3. It has been said that offense wins games, but defense wins championships. The final unlock in winning a game comes down to the influential impact of large defensive plays. The presence of a `defensive touchdown`, particularity via an `interception`, helps influence the outcome. 

These insights can be used by coaches and players alike to help them win games and set themselves up for future and current success. A rising tide raises all boats - if the team wins, the individuals will win. A highly sought after recruit is better off going to a program where there individual contribution can be spotlighted *as well as* winning games for the team. With these three areas as focus, teams can be better on their way towards success. 

### **Objective 2 (Draft Status)**
Being drafted in the NFL is every college football players dream. Moving from making money only via NIL to having a salary and performing at the highest level pushes players to work as hard as possible. However, the success rate for many is difficult. With these insights, hopefully prospects will have a better idea of what they need to do in order to end up being drafted. 

1. 



### **Objective 3 (Press Sentiment)**



## **Dataset Information**



## **Methods**



## **Results**



## **Conclusions**



## **Limitations & Future Research**
