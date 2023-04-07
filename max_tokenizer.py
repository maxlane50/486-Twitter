import sys
import os
import math

contractions_dict = {
    "aren't": "are not",
    "can't": "cannot",
    "couldn't": "could not",
    "didn't": "did not",
    "don't": "do not",
    "hadn't": "had not",
    "haven't": "have not",
    "he's": "he is",
    "he'll": "he will",
    "he'd": "he would",
    "here's": "here is",
    "I'm": "I am",
    "I've": "I have",
    "I'll": "I will",
    "I'd": "I has",
    "isn't": "is not",
    "it is": "it's",
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
    "they'd": "they had",
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

def tokenizeText(input):
    # remove whitespace right off the bat, now only deal with other stuff
    raw_list = input.split()
    tokenized_list = []
    #print(raw_list)
    for token in raw_list:
        cur_token = ''
        added_contraction = False
        for i in range(len(token)):
            temp_token = token[i]
            if token[i].isupper():
                temp_token = temp_token.lower()
            if temp_token == ',':
                if (i != len(token) - 1) and (token[i+1]).isnumeric(): # is a number
                    cur_token += temp_token
                else: #isn't a number
                    tokenized_list.append(cur_token)
                    cur_token = ','
            elif temp_token == '.':
                if i != len(token) - 1:
                    cur_token += temp_token 
                else:
                    tokenized_list.append(cur_token)
                    cur_token = '.'
            elif temp_token == "'":
                if i != len(token) - 1:
                    if not token[i].isupper() and i == len(token) - 2 and token[i+1] == 's': #if first letter is capitalized as well as the last letter being 's', likely possessive
                        tokenized_list.append(cur_token)
                        cur_token = "'"
                    else: #likely contraction
                        if token in contractions_dict:
                            expanded_tok = contractions_dict[token]
                            contraction_list = expanded_tok.split()
                            tokenized_list.append(contraction_list[0])
                            if len(contraction_list) == 2:
                                tokenized_list.append(contraction_list[1]) # add second word to token list
                            added_contraction = True
                        else: #ignore it if not in dict
                            cur_token += temp_token
                else:
                    tokenized_list.append(cur_token)
                    cur_token = "'"
            else:
                cur_token += temp_token
        if not added_contraction: # avoid double adding tokens w/ contractions
            if token != '.' and token != ',' and token != "'":
                tokenized_list.append(cur_token)
    
    if "." in tokenized_list:
        tokenized_list.remove('.')
    if "," in tokenized_list:
        tokenized_list.remove(',')
    return tokenized_list