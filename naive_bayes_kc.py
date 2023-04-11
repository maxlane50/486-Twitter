# Kathryn Kennedy; kcken

import sys
import os
import re
import csv
import math

def main():
    filepath = sys.argv[1]
    file_string = filepath.replace('/', '')
    output_file = open(f"naivebayes.output.{file_string}", 'w')
    file_list = []
    num_docs = 0
    for file in os.listdir(filepath):
        file_list.append(file)
        num_docs += 1     
    
    # 
    len_of_test = math.floor(0.1*num_docs)
    for x in range(10):
        test_list = file_list.copy()
        train_list = file_list.copy()
        if x == 9:
            test_list = test_list[(len_of_test*x):]                
        else:
            test_list = test_list[(len_of_test*x):(len_of_test*(x+1))]
        train_list = [y for y in file_list if y not in test_list]
        prob_true, prob_fake, true_probs, fake_probs = trainNaiveBayes(filepath, train_list)
        
        if x == 0:
            sorted_true_probs = sorted(true_probs.items(), key=lambda x:x[1], reverse=True)
            sorted_fake_probs = sorted(fake_probs.items(), key=lambda x:x[1], reverse=True)
            for y in range(10):
                print(f"true: {sorted_true_probs[y]}")
            for z in range(10):
                print(f"false: {sorted_fake_probs[z]}")
        for file in test_list:                
            output_file.write(f"{file}\t")
            ans = testNaiveBayes(filepath, file, prob_true, prob_fake, true_probs, fake_probs)
            output_file.write(f"{ans}\n")   
        print(x)        

def trainNaiveBayes(filepath, file_list):
    vocab = []
    vocab_count = 0
    num_fake_words = 0
    num_true_words = 0
    prob_fake = 0
    prob_true = 0
    num_docs = 0
    # Dictionary of nk values for fake
    fake_text = {}
    # Dictionary of nk values for true
    true_text = {}
    fake_probs = {}
    true_probs = {}

    # Traverse through each file in the file list
    for file in file_list:
        openfile = filepath + file
        num_docs += 1
        status = ""

        # Count number of files that are fake and that are true
        if re.search("fake", file):
            prob_fake += 1
            status = "fake"
        if re.search("true", file):
            prob_true += 1    
            status = "true"

        with open(openfile, encoding="ISO-8859-1") as o_file:
            data = o_file.read()
            token_list = tokenizeText(data)
            # Traverse through each word in file
            for word in token_list:
                # Calculate the vocab of the dataset
                if word not in vocab:
                    vocab.append(word)
                    vocab_count += 1
                
                # Add to total num fake words
                # Add to fake dict
                if status == "fake":
                    num_fake_words += 1
                    if word in fake_text:
                        fake_text[word] += 1
                    else:
                        fake_text[word] = 1

                # Increase total num true words
                # Add to true dict
                if status == "true":
                    num_true_words += 1
                    if word in true_text:
                        true_text[word] += 1
                    else:
                        true_text[word] = 1       

    # Class probabilities
    prob_fake = prob_fake / num_docs
    prob_true = prob_true / num_docs
    nktrue = 0
    nkfake = 0

    # For each word in true vocab and each word in fake vocab
    for word in vocab:
        if word in fake_text:
            nkfake = fake_text[word]
        if word in true_text:
            nktrue = true_text[word]
        # Make dict of probs for each word in true and fake vocab
        fake_probs[word] = math.log((nkfake + 1) / (num_fake_words + vocab_count))
        true_probs[word] = math.log((nktrue + 1) / (num_true_words + vocab_count))

    # Returning percent of docs that are true, percent fake, 
    # a dict of all true probs, and dict of fake probs   
    return prob_true, prob_fake, true_probs, fake_probs

def testNaiveBayes(filepath, test_file, prob_true, prob_fake, true_probs, fake_probs):
    true = abs(math.log(prob_true))
    fake = abs(math.log(prob_fake))
    openfile = filepath + test_file
    with open(openfile, encoding="ISO-8859-1") as o_file:
        data = o_file.read()
        token_list = tokenizeText(data)
        for word in token_list:
            if word in true_probs:
                true *= abs(true_probs[word])
                # print(true)
            if word in fake_probs:
                fake *= abs(fake_probs[word])

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



if __name__ == "__main__":
    main()  