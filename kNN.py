import sys
import os
import math
import csv
import string
import numpy as np
import re
import pandas as pd


def tokenizeText(inputText):
    # contractions dict
    contractions = {
        "aren't": "are not",
        "can't": "cannot",
        "couldn't": "could not",
        "didn't": "did not",
        "don't": "do not",
        "doesn't": "does not",
        "hadn't": "had not",
        "haven't": "have not",
        "he's": "he is",
        "he'll": "he will",
        "he'd": "he would",
        "here's": "here is",
        "I'm": "I am",
        "I've": "I have",
        "I'll": "I will",
        "I'd": "I would",
        "isn't": "is not",
        "it's": "it is",
        "it'll": "it will",
        "mustn't": "must not",
        "she's": "she is",
        "she'll": "she will",
        "she'd": "she had",
        "shouldn't": "should not",
        "that's": "that is",
        "there's": "there is",
        "they're": "they are",
        "they've": "they have",
        "they'll": "they will",
        "they'd": "they would",
        "wasn't": "was not",
        "we're": "we are",
        "we've": "we have",
        "we'll": "we will",
        "we'd": "we would",
        "weren't": "were not",
        "what's": "what is",
        "where's": "where is",
        "who's": "who is",
        "who'll": "who will",
        "won't": "will not",
        "wouldn't": "would not",
        "you're": "you are",
        "you've": "you have",
        "you'll": "you will",
        "you'd": "you would"
    }

    tempList = inputText.split()
    num = 0
    while num < len(tempList):
        x = tempList[num]
        if x == '':
            num += 1
            continue

        if (x[len(x) - 1] == "," or x[len(x) - 1] == "!" or x[len(x) - 1] == "'" or x[len(x) - 1] == "?" or x[
            len(x) - 1] == "/") and not (x[len(x) - 2].isupper()) and len(x) > 1:  # punctuation at the end of a word

            tempList[num] = x[:len(x) - 1]
            tempList.insert(num + 1, x[len(x) - 1:])
            continue

        if (x[0] == "," or x[0] == "." or x[0] == "!" or x[0] == "?" or x[0] == "/") and len(
                x) > 1:  # punctuation at the beginning of a word
            tempList[num] = x[0]
            tempList.insert(num + 1, x[1:])
            continue

        if (x[0] == "'") and len(x) > 1 and x != "'s":  # possessive
            tempList[num] = x[0]
            tempList.insert(num + 1, x[1:])
            continue

        index = x.find(",")
        if index != -1 and index != len(x) - 1 and index != 0:  # comma in middle of letters
            if not (x[index - 1].isdigit() and x[index + 1].isdigit()):
                tempList[num] = x[0:index]
                tempList.insert(num + 1, x[index:index + 1])
                tempList.insert(num + 2, x[index + 1:])
                continue

        index = x.find(".")
        if index != -1 and index != len(x) - 1 and index != 0:  # period in middle of letters
            if x[0:index] == "Dr" or x[0:index] == "Mr" or x[0:index] == "Ms" or x[0:index] == "Mrs":
                tempList[num] = x[0:index + 1]
                tempList.insert(num + 1, x[index + 1:])
            elif not (x[index - 1].isupper() and x[index + 1].isupper()):
                tempList[num] = x[0:index]
                tempList.insert(num + 1, x[index:index + 1])
                tempList.insert(num + 2, x[index + 1:])
                continue

        if (x[len(x) - 1] == ".") and len(x) > 2 and (
                x != "Dr." and x != "Mr." and x != "Ms." and x != "Mrs."):  # abbreveations
            tempList[num] = x[:len(x) - 1]
            tempList.insert(num + 1, x[len(x) - 1])
            continue

        # contractions
        index = x.find("'")
        if index != -1 and index != len(x) - 1 and index != 0:  # ' in middle of letters
            if contractions.get(x):
                contList = contractions[x].split(' ')
                tempList[num] = contList[0]
                z = 0
                for cont in contList:
                    if z > 0:
                        tempList.insert(num + z, cont)
                    z += 1
                continue
            elif index == len(x) - 2 and x[len(x) - 1] == "s":
                tempList[num] = x[0:index]
                tempList.insert(num + 1, x[index:])
            else:
                tempList[num] = x[0:index]
                tempList.insert(num + 1, x[index:index + 1])
                tempList.insert(num + 2, x[index + 1:])
                continue

        num += 1
    return tempList


def removeStopWords(tokenList):
    stopWords = ["a", "all", "an", "and", "any", "are", "as", "at", "be", "been", "but", "by", "few", "from", "for",
                 "have", "he", "her", "here", "him", "his", "how", "i", "in", "is", "it", "its", "many", "me", "my",
                 "none", "of", "on", "or", "our", "she", "some", "the", "their", "them", "there", "they", "that",
                 "this", "to", "us", "was", "what", "when", "where", "which", "who", "why", "will", "with", "you",
                 "your"]
    num = 0
    while num < len(tokenList):
        if stopWords.count(tokenList[num]) > 0:
            tokenList.pop(num)
            continue
        num += 1
    return tokenList

def extract_word_custom(input_string,n_gram = 1):

    # TODO: Implement this function
    input_string = re.sub(r"http\S+", "", input_string)

    for ch in string.punctuation:
        if ch != '#' and ch != "@":
            input_string = input_string.replace(ch, " ")
    input_string = input_string.lower()
    input_string = input_string.replace("rt"," ")
    z = input_string.split()

    nGramWords = []
    if len(z) != 0:

        if z[len(z)-1][len(z[len(z)-1])-1:] == "…":
            z[len(z)-1] = z[len(z)-1][0:len(z[len(z)-1])-1]


        if n_gram > 1:
            soloWords = input_string.split()
            nGramWords = [' '.join(soloWords[i: i+n_gram]) for i in range(0,len(soloWords),1)]
            z = []
    comb = np.concatenate((z,nGramWords))
    return comb

#create dict of unique words in the dataset
def extract_dictionary_custom(df,n_gram = 1):

    word_dict = {}
    # TODO: Implement this function
    ind = 0

    num_of_tweets = 0
    for index, row in df.iterrows():
        x = extract_word_custom(row["Tweet"],n_gram)
        if len(x) != 0:
            num_of_tweets += 1
            for word in x:
                if word not in word_dict:
                    word_dict[word] = ind
                    ind+=1
    return word_dict, num_of_tweets

#generate a feature matrix
def trainkNN(df):
    word_dict, num_of_tweets = extract_dictionary_custom(df,1)
    labels = {}
    num_of_words = len(word_dict)
    feature_matrix = np.zeros((num_of_tweets,num_of_words))
    ind = 0
    for index, row in df.iterrows():
        x = extract_word_custom(row["Tweet"],1)
        y = row["Party"]
        if len(x) != 0:
            for word in x:
                if word in word_dict:
                    feature_matrix[ind][word_dict[word]] += 1
            labels[ind] = y
            ind +=1
    return feature_matrix, labels, word_dict

def trainTestData(df,word_dict):
    labels = {}
    feature_matrix = np.zeros((len(df),len(word_dict)))
    ind = 0
    for index, row in df.iterrows():
        x = extract_word_custom(row["Tweet"],1)
        y = row["Party"]
        for word in x:
            if word in word_dict:
                feature_matrix[ind][word_dict[word]] += 1
        labels[ind] = y
        ind += 1
    return feature_matrix, labels


def testkNN(feature_matrix, test_feature_matrix, trainLabels, testLabels,k):
    total = len(test_feature_matrix)
    accurate = 0
    for t in range(len(test_feature_matrix)):
        answer = testLabels[t]
        eucDist = {}
        for x in range(len(feature_matrix)):
            eucDist[math.dist(feature_matrix[x],test_feature_matrix[t])] = trainLabels[x]
        newDict = dict(sorted(eucDist.items()))
        count = 0
        potLabels = []
        for el in newDict:
            potLabels.append(newDict[el])
            count += 1
            if count == k:
                break
        guess = max(set(potLabels), key = potLabels.count)
        if guess == answer:
            accurate += 1
    return accurate/total







def main(argv):
    trainSet = argv[1]
    # testSet = argv[2]
    # print(trainSet)
    # print(testSet)
    df = pd.read_csv(trainSet,delimiter=",")
    df = df.sample(frac = 0.10, random_state=200)
    # print(len(df))
    traindf = df.sample(frac = 0.85, random_state=200)
    # print(len(traindf))
    testdf = df.drop(traindf.index)
    # print(len(testdf))
    feature_matrix, trainLabels, word_dict = trainkNN(traindf)
    test_feature_matrix, testLabels = trainTestData(testdf,word_dict)
    # print(test_feature_matrix.sum(axis = 1))
    print(testkNN(feature_matrix,test_feature_matrix, trainLabels, testLabels,20))

if __name__ == '__main__':
    main(sys.argv)


# def trainNaiveBayes(trainFiles,path):
#     fakeDocs = 0
#     trueDocs = 0
#     totDocs = 0
#     fakeWordDict = {}
#     trueWordDict = {}
#     fakeWordCount = 0
#     trueWordCount = 0
#     vocab = {}
#     vocabSize = 0

#     for file in trainFiles:
#         file_path = f"{path}{file}"
#         file1 = open(file_path,'r',encoding="utf8")
#         text = file1.read()
#         tokens = tokenizeText(text)
#         noStopWords = removeStopWords(tokens)
#         if file[0] == 'f':
#             fakeDocs += 1
#             for word in noStopWords:
#                 fakeWordCount += 1
#                 if word not in fakeWordDict:
#                     fakeWordDict[word] = 1
#                 else:
#                     fakeWordDict[word] += 1

#                 if word not in vocab:
#                     vocab[word] = 1
#                     vocabSize +=1
#                 else:
#                     continue
#         else:
#             trueDocs += 1
#             for word in noStopWords:
#                 trueWordCount += 1
#                 if word not in trueWordDict:
#                     trueWordDict[word] = 1
#                 else:
#                     trueWordDict[word] += 1

#                 if word not in vocab:
#                     vocab[word] = 1
#                     vocabSize +=1
#                 else:
#                     continue
#         totDocs +=1



#     probFake = fakeDocs/totDocs
#     probTrue = trueDocs/totDocs
#     probs = [probFake,probTrue]


#     return probs, vocabSize, fakeWordDict, trueWordDict, fakeWordCount, trueWordCount

# def testNaiveBayes(testFile, probs, vocabSize, fakeWordDict, trueWordDict, fakeWordCount, trueWordCount,path):
#     file_path = f"{path}{testFile[0]}"
#     file1 = open(file_path, 'r',encoding="utf8")
#     text = file1.read()
#     tokens = tokenizeText(text)
#     testWords = removeStopWords(tokens)

#     probFakeSum = 0
#     probTrueSum = 0
#     for word in testWords:
#         valFake = 0
#         valTrue = 0
#         if word in fakeWordDict:
#             valFake = fakeWordDict[word]
#         if word in trueWordDict:
#             valTrue = trueWordDict[word]
#         probFakeSum += (valFake + 1)/(fakeWordCount + vocabSize)
#         probTrueSum += (valTrue + 1)/(trueWordCount + vocabSize)
#     fakeProb = probs[0]*probFakeSum
#     trueProb = probs[1]*probTrueSum
#     if fakeProb > trueProb:
#         return "fake"
#     return "true"


