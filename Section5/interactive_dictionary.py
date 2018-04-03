import json
from difflib import get_close_matches

# create data object by loading and reading the dictionary.json file
# this will create a dict data type
data = json.load(open("data.json","r"))
#print(type(data))

def definition(word):
    # Account for names like Delhi
    if not str.upper(word[0]):
        # make all words lower case to match case in data.json
        word = word.lower()
    else:
        # make sure the word is in data.json file
        # if the word is in the data.json file then return the definition
        if word in data:
            # the results come back as a list
            #print(type(data[word]))
            return data[word]
        # if the word is not found as it is spelt try to find a close approximation and ask if 
        # that is the word they are looking for
        elif len(get_close_matches(word,data.keys())) > 0:
            yn = input("Did you mean %s instead? Y or N " % get_close_matches(word, data.keys())[0])
            yn = yn.upper()
            if yn == "Y":
                word = get_close_matches(word, data.keys())[0]
                return data[word]
            elif yn == "N":
                return "Please search another word we can't find %s " % word
            else:
                return "We did not understand your query, please try again"
        # if all else fails, then tell them the word is not in the dictionary
        else:
            return "%s is not in the dictionary, please recheck the word" % word
    
word = input("Enter word: ")
output = definition(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
