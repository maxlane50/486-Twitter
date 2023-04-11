# Kathryn Kennedy; kcken

import sys
import os
import re
import csv
import math
from process_csv import *

def main():
    filename = 'ExtractedTweets.csv'
    output_file = open(f"naivebayes.output", 'w')
    # Dictionary containing all tweets from spreadsheet
    # Structure:
    #   Example entry --> {"Democrat": ["tweet 1 example", "tweet 2 example", ...]}
    #   Only contains two keys, either Republican or Democrat w/ array of tweets following
    tweets_dict = process_csv(filename)
    num_rep_docs = len(tweets_dict['Republican'])
    num_dem_docs = len(tweets_dict['Democrat'])
    print(num_dem_docs)
    print(num_rep_docs)
    num_docs = num_rep_docs + num_dem_docs
    rep_array = tweets_dict['Republican']
    dem_array = tweets_dict["Democrat"]

    # Leave One Out Evaluation Strategy
    # 10 iterations, first uses first 10% as test, other 90% to train
    len_of_test = math.floor(0.1*num_docs)
    for x in range(10):
        test_list_r = rep_array.copy()
        test_list_d = dem_array.copy()
        train_list_r = rep_array.copy()
        train_list_d = dem_array.copy()
        # If we are at the last iteration, read to the end of the array
        if x == 9:
            test_list_r = test_list_r[(len_of_test*x):]
            test_list_d = test_list_d[(len_of_test*x):]               
        else:
            test_list_r = test_list_r[(len_of_test*x):(len_of_test*(x+1))]
            test_list_d = test_list_d[(len_of_test*x):(len_of_test*(x+1))]
        train_list_r = [y for y in rep_array if y not in test_list_r]
        train_list_d = [y for y in dem_array if y not in test_list_d]
        prob_rep, prob_dem, rep_probs, dem_probs = trainNaiveBayes(train_list_r, train_list_d)
        
        if x == 0:
            sorted_true_probs = sorted(rep_probs.items(), key=lambda x:x[1], reverse=True)
            sorted_fake_probs = sorted(dem_probs.items(), key=lambda x:x[1], reverse=True)
            for y in range(10):
                print(f"true: {sorted_true_probs[y]}")
            for z in range(10):
                print(f"false: {sorted_fake_probs[z]}")
        for tweet in test_list_r:                
            output_file.write("rep\t")
            ans = testNaiveBayes(tweet, prob_rep, prob_dem, rep_probs, dem_probs)
            output_file.write(f"{ans}\n")
        for tweet in test_list_d:                
            output_file.write("dem\t")
            ans = testNaiveBayes(tweet, prob_rep, prob_dem, rep_probs, dem_probs)
            output_file.write(f"{ans}\n")  
        print(x)        

def trainNaiveBayes(rep_array, dem_array):
    vocab = []
    vocab_count = 0
    num_dem_words = 0
    num_rep_words = 0
    prob_dem = 0
    prob_rep = 0
    num_docs = 0
    # Dictionary of nk values for dem
    dem_text = {}
    # Dictionary of nk values for rep
    rep_text = {}

    dem_probs = {}
    rep_probs = {}

    # Traverse through each republican tweet in the tweet list
    for tweet in rep_array:
        num_docs += 1
        prob_rep += 1
        token_list = removeStopwords(tokenizeText(tweet))

        # Traverse through each word in file
        for word in token_list:
            # Calculate the vocab of the dataset
            if word not in vocab:
                vocab.append(word)
                vocab_count += 1

            # Increase total num rep words
            # Add to rep dict
            num_rep_words += 1
            if word in rep_text:
                rep_text[word] += 1
            else:
                rep_text[word] = 1

    # Traverse through each democrat tweet in the tweet list
    for tweet in dem_array:
        num_docs += 1
        prob_dem += 1
        token_list = removeStopwords(tokenizeText(tweet))
        # Traverse through each word in file
        for word in token_list:
            # Calculate the vocab of the dataset
            if word not in vocab:
                vocab.append(word)
                vocab_count += 1

            # Increase total num dem words
            # Add to dem dict
            num_dem_words += 1
            if word in dem_text:
                dem_text[word] += 1
            else:
                dem_text[word] = 1     

    # Class probabilities
    prob_dem = prob_dem / num_docs
    prob_rep = prob_rep / num_docs
    nkrep = 0
    nkdem = 0

    # For each word in true vocab and each word in fake vocab
    for word in vocab:
        if word in dem_text:
            nkdem = dem_text[word]
        if word in rep_text:
            nkrep = rep_text[word]
        # Make dict of probs for each word in true and fake vocab
        dem_probs[word] = math.log((nkdem + 1) / (num_dem_words + vocab_count))
        rep_probs[word] = math.log((nkrep + 1) / (num_rep_words + vocab_count))

    # Returning percent of docs that are true, percent fake, 
    # a dict of all true probs, and dict of fake probs   
    return prob_rep, prob_dem, rep_probs, dem_probs

def testNaiveBayes(tweet, prob_rep, prob_dem, rep_probs, dem_probs):
    true = math.log(prob_rep)
    fake = math.log(prob_dem)    
    token_list = removeStopwords(tokenizeText(tweet))
    for word in token_list:
        if word in rep_probs:
            # Switched to addition here
            true += rep_probs[word]
            # print(true)
        if word in dem_probs:
            # Switched to addition here
            fake += dem_probs[word]

    if true > fake:
        return "true"
    elif fake > true:
        return "fake"
    else:
        return "equal"
 
def tokenizeText(text):
    cont_dict = {}

    with open('contractions.csv', 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            cont_dict[row[0]] = row[1]
    for word in text.split():
        if word in cont_dict.keys():
            text = text.replace(word, cont_dict[word])

    #Removes all punctuation except for punctuation between digits.
    expression = "(?<!\d)[.,;:](?!\d)"
    text = re.sub(expression, '', text)
    text = re.sub("('s)", '', text)
    text = text.replace('"', '')
    text = text.replace("'", '')
    text = text.lower()
    token_list = text.split()
    return token_list

def removeStopwords(token_list):
    s = []
    with open('stopwords.txt', 'r') as stopfile:
        for word in stopfile:
            word = word.split('\n')
            s.append(word[0])
    p = [t for t in token_list if t not in s]
    return p



if __name__ == "__main__":
    main()  