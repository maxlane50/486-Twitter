# 486-Twitter
This README serves as documentation for how our code is laid out and how it can be used.

Overview:
Our overall goal is to take tweets made by members of the United States government, and classify their tweets into either Republican or Democratic based on the content of their tweets and training data. We used multiple methods to classify tweets as either Democratic or Republican, such as nearest neighbor and Naive Bayes.

Data in the Repository:
We have two data sets in this repository to use, with the distinct different being the time they were published. Thanks to a GSI in EECS 486, we obtained a dataset in .csv format from Kaggle, with more than 70000 tweets made by government officials that were tagged with a label of either Republican or Democratic titled "ExtractedTweets.csv". This dataset however only contains tweets from pre-2016. Because of this, we compiled a dataset from 81 current Congress members pulling their 200 most recent tweets, resulting in ~16000 tweets that are more based on current events. This dataset is titled ScrapedCurrentTweets.csv, and is also tagged with the political party associated with the tweet. The only difference between the two information wise is the fact that the current tweets dataset does not include the Twitter username of the user who made the tweet as we deemed this unimportant for our purposes.

Scraping code: