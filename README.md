# 486-Twitter
This README serves as documentation/explanation for how our code is laid out and how it can be used.

## Overview
Our overall goal is to take tweets made by members of the United States government, and classify their tweets into either Republican or Democratic based on the content of their tweets and training data. We used multiple methods to classify tweets as either Democratic or Republican, such as nearest neighbor and Naive Bayes.

## Data in the Repository
We have two data sets in this repository to use, with the distinct different being the time they were published. Thanks to a GSI in EECS 486, we obtained a dataset in .csv format from Kaggle, with more than 70000 tweets made by government officials that were tagged with a label of either Republican or Democratic titled "ExtractedTweets.csv". This dataset however only contains tweets from pre-2016. Because of this, we compiled a dataset from 81 current Congress members pulling their 200 most recent tweets, resulting in ~16000 tweets that are more based on current events. This dataset is titled "ScrapedCurrentTweets.csv", and is also tagged with the political party associated with the tweet. The only difference between the two information wise is the fact that the current tweets dataset does not include the Twitter username of the user who made the tweet as we deemed this unimportant for our purposes.

## Scraping Code
In scrape_current_politicians.py, we utilized the snscrape module allowing us to bypass the Twitter paid API and scrape tweets from current members of Congress. The dictionary of usernames that is used comes from fetch_cur_tweets_dict.py, and this dictionary was assembled manually. The program iterates through each username and scrapes their page one at a time, and after this data is retrieved it is written one by one into a .csv file with the Python "csv" module, tagging it with the political party as well.

## CSV Processing
The goal of the process_csv.py file is to take the .csv file format and then process it into a data structure that makes it significantly easier to use for our classifying methods. The program takes one row from the file at a time, eliminates unnecessary quotation marks, ellipses, and links to the tweet, and then using the tag its associated with, places it into a dictionary with the key being the political party and the value being an array of tweets associated with that party. The main function "process_csv" takes the filename as the argument and returns the dictionary as a result.
