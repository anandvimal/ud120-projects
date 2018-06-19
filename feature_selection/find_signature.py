#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl"
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )


### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]

### your code goes here
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

#check accuracy here
from sklearn.metrics import accuracy_score
score_p = accuracy_score(labels_test, pred)


print "length of features_train : ", len(features_train)
print "accuracy_score is :",score_p
print "features number",clf.feature_importances_

counter = 0
for i in clf.feature_importances_:
    counter = counter + 1

    if i != 0.0:
        print counter," : ",i


max_index = 0
counter = 0
max_element = 0


for i in clf.feature_importances_:
    if i > max_element:
        max_element = i
        max_index = counter
    counter = counter+1


print ("max element:",max_element)
print ("max index:",max_index)


'''
#print( word_data )
counter = 0
for i in word_data:
    #print i
    print"\ncounter = ",counter
    counter = counter +1
    if(counter == 33614):
        print i
'''


'''
for i in features_train:
    print i
    print" \n"
'''
#print features_train
#print word_data[]
