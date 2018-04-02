import json
from difflib import get_close_matches

# create data object by loading and reading the dictionary.json file
# this will create a dict data type
data = json.load(open("data.json","r"))
#print(type(data))

def definition(word):
    # make all words lower case to match case in data.json
    word = word.lower()
    # make sure the word is in data.json file
    if word in data:
        # the results come back as a list
        #print(type(data[word]))
        return data[word]
    else:
        return "That word is not in the dictionary, please recheck the word"
    
word = input("Enter word: ")

print(definition(word))
