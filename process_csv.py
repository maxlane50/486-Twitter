def process(filename):
    # Dictionary containing all tweets from spreadsheet
    # Structure:
    #   Example entry --> {"Democrat": ["tweet 1 example", "tweet 2 example", ...]}
    #   Only contains two keys, either Republican or Democrat w/ array of tweets following
    tweets_dict = {}

    with open(filename) as opened_csv:
        read_csv = opened_csv.read()
        csv_list = read_csv.split('\n')
        
        for i in range(len(csv_list)):
            temp_array = csv_list[i].split(',')
            if temp_array[0] == "Democrat":
                if ("Democrat" not in tweets_dict):
                    tweets_dict["Democrat"] = []
                tweets_dict["Democrat"].append(temp_array[2]) # add cur tweet to array
            elif temp_array[0] == "Republican":
                if ("Republican" not in tweets_dict):
                    tweets_dict["Republican"] = []
                tweets_dict["Republican"].append(temp_array[2]) # add cur tweet to array
            else: #Don't think this will ever happen
                print(temp_array[0])

            if (i == 100):
                print(tweets_dict)
                break


def main():
    process('ExtractedTweets.csv')

main()