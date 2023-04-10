
# Potentially could add removal of stopwords/stemming/tokenizing here
# For now will just remove quotations/ellipses/emojis
def process_tweet(tweet):
    if (tweet[0] == '"'):
        tweet = tweet[1:] # get rid of quotation mark to start tweet
    
    ellipsis_loc = tweet.find("…")
    if (ellipsis_loc != -1):
        tweet = tweet[:ellipsis_loc]

    link_loc = tweet.find("https")
    if (link_loc != -1):
        tweet = tweet[:link_loc]

    return tweet

def find_political_party(tweet):
    first_comma = tweet.find(',')
    political_party = tweet[0:first_comma]
    first_comma += 1
    rest_of_tweet = tweet[first_comma:]
    second_comma = rest_of_tweet.find(',')
    second_comma += 1
    actual_tweet = rest_of_tweet[second_comma:] # don't care about their twitter handle, get rid of it
    print(actual_tweet)
    return political_party, actual_tweet

def process_csv(filename):
    # Dictionary containing all tweets from spreadsheet
    # Structure:
    #   Example entry --> {"Democrat": ["tweet 1 example", "tweet 2 example", ...]}
    #   Only contains two keys, either Republican or Democrat w/ array of tweets following
    tweets_dict = {}

    with open(filename) as opened_csv:
        read_csv = opened_csv.read()
        csv_list = read_csv.split('\n')
        
        for i in range(len(csv_list)):
            political_party, actual_tweet = find_political_party(csv_list[i])
            if political_party == "Democrat":
                if ("Democrat" not in tweets_dict):
                    tweets_dict["Democrat"] = []
                tweets_dict["Democrat"].append(process_tweet(actual_tweet)) # add cur tweet to array post processing
            elif political_party == "Republican":
                if ("Republican" not in tweets_dict):
                    tweets_dict["Republican"] = []
                tweets_dict["Republican"].append(process_tweet(actual_tweet)) # add cur tweet to array post processing
            else: #Don't think this will ever happen
                print(political_party)

    return tweets_dict


def main():
    process_csv('ExtractedTweets.csv')

main()