import snscrape.modules.twitter as sntwitter
import pandas as pd
import csv
from fetch_cur_tweets_dict import get_cur_tweets_dict

# Manually researched list of Twitter usernames for current politicians
def scrape_single_page(username):
    username = "from:" + username
    scraper = sntwitter.TwitterSearchScraper(username)
    count = 0
    for tweet in scraper.get_items():
        print(tweet.content)
        count += 1
        if count > 100:
            break

def main():
    username_dict = get_cur_tweets_dict()
    #Republicans
    for username in username_dict["Republican"]:
        pass
    #Democrats
    for username in username_dict["Democrat"]:
        pass

main()