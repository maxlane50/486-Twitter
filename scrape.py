import snscrape.modules.twitter as sntwitter
import pandas as pd

def main():
    scraper = sntwitter.TwitterSearchScraper('from:elonmusk')
    count = 0
    for tweet in scraper.get_items():
        print(tweet.content)
        count += 1
        if count > 100:
            break

main()