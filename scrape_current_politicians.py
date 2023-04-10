import snscrape.modules.twitter as sntwitter
import pandas as pd
import csv
from fetch_cur_tweets_dict import get_cur_usernames_dict


def scrape_single_page(username):
    username = "from:" + username
    scraper = sntwitter.TwitterSearchScraper(username)
    return scraper.get_items()
    # for tweet in scraper.get_items():
    #     print(tweet.content)
    #     count += 1
    #     if count > 100:
    #         break

def main():
    with open('ScrapedCurrentTweets.csv', 'w', newline='\n') as file:
        writer = csv.writer(file)
        username_dict = get_cur_usernames_dict()
        #Republicans
        count = 0
        for username in username_dict["Republican"]:
            tweets = scrape_single_page(username)
            tweet_count = 0
            for tweet in tweets:
                writer.writerow(["Republican", tweet.content])
                tweet_count += 1
                if tweet_count == 200:
                    break
            count += 1
            print(count)
        #Democrats
        count = 0
        for username in username_dict["Democrat"]:
            tweets = scrape_single_page(username)
            tweet_count = 0
            for tweet in tweets:
                writer.writerow(["Democrat", tweet.content])
                tweet_count += 1
                if tweet_count == 200:
                    break
            count += 1
            print(count)

main()

