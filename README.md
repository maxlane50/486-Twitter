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

## Naive Bayes
The naive_bayes.py file takes the data structure from process_csv.py and runs the Multinomial Naive Bayes classifier on it. It uses the Leave-One-Out strategy, where it takes 10% of the data, trains on 90% of the 10% and tests on 10% of the 10%, and does that 10 total times. This makes the classifier run significantly faster than just training on 90% of the data and testing on 10%. The function trainNaiveBayes() trains the classifier given an array of tweets by republicans and an array of tweets by democrats. It outputs two dictionaries which contain each word in the vocab and the probability of that word for either a republican or democrat tweet. The testNaiveBayes() function takes in one tweet and tests whether it is more likely to come from a republican or democrat. The program writes to an output in the format of{correct_answer}: {predicted_answer}

## K-Nearest Neighbor

The kNN.py file takes in 4 arguments from the command line. The dataset to be tested on, the similarity metric, the k value, and the number of n-grams. A sample line to run the program would be 'python kNN.py ScrapedCurrentTweets.csv 1 2'. This would test on the scraped tweets dataset for 1 nearest neighbor with n-grams = 2. Once the code is run it partitions the dataset into a training and testing set (85-15 split). The accuracy of classifier is tested on the test set. Using either jaccard similarity of eculidean distance the closest training tweets are obatined for a test  tweet. The majority label of the nearested neighbors is used to predict the test tweet. The accuracy of all the predicitions is then output to the terminal.