#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

from sklearn.feature_extraction.text import TfidfVectorizer

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker
temp_counter = 0


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        #temp_counter += 1
        #if temp_counter < 200:
            path = os.path.join('..', path[:-1])
            print path
            email = open(path, "r")

            ### use parseOutText to extract the text from the opened email
            parsed_email = parseOutText(email)
            ### use str.replace() to remove any instances of the words
            ### ["sara", "shackleton", "chris", "germani"]
            '''
            parsed_email.replace( "sara" ,"")
            parsed_email.replace( "shackleton" ,"")
            parsed_email.replace( "chris" ,"")
            parsed_email.replace( "germani" ,"")
            '''
            for w in ["sara", "shackleton", "chris", "germani","sshacklensf","cgermannsf"]:
                if w in parsed_email:
                    parsed_email = parsed_email.replace(w, '')

            ### append the text to word_data
            word_data.append(parsed_email)
            #print(parsed_email)
            #print(name)
            #print("####################################")
            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
            if name == "sara" :
                from_data.append(0)
                #print(0)
            else:
                from_data.append(1)
                #print(1)

            email.close()

#print(word_data[151])
#print(word_data[152])
#print(word_data[153])
#print "emails processed"

from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )





### in Part 4, do TfIdf vectorization here

from sklearn.feature_extraction.text import TfidfVectorizer
word_data = pickle.load(open("your_word_data.pkl", "rb"))
#word_data = pickle.load(open("real_your_word_data.pkl", "rb"))
word_data = pickle.load(open("your_word_data.pkl", "rb"))

vectorizer = TfidfVectorizer(stop_words='english')

vectorizer.fit_transform(word_data)
#print( vectorizer.get_stop_words() )
unique = vectorizer.get_feature_names()
print( "length of feature_names is : ",len(unique))


'''import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
word_data = pickle.load(open("your_word_data.pkl", "rb"))

print "len:", len(word_data)

vectorizer = TfidfVectorizer(stop_words="english")
vectorizer.fit_transform(word_data)

unique = vectorizer.get_feature_names()

print "How many unique words are in your TfIdf?", len(unique)
'''
for x in range(34590, 34600):
    print x, unique[x]

# for our solution 34595 works as answer even in quiz we are asked to submit 34597.
# it is probably because our unique words are also 2 less than what was right answer.
print('q21 answer is : ',unique[34597])




#
