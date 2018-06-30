#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#37 making decision tree classifier run with
from sklearn import tree
from sklearn.metrics import accuracy_score



#print("number of entries in data",len(features_train))
print("number of features in data",len(features_train[0]))


#create decision tree classifier with min_samples_split = 40
clf = tree.DecisionTreeClassifier(min_samples_split=40)
clf = clf.fit(features_train, labels_train)

y_pred = clf.predict(features_test)

#accuracy_score(y_true, y_pred)
accuracy = accuracy_score(labels_test, y_pred)

print("accuracy at min_samples_split:40 with decision tree is",accuracy)
#########################################################

'''
accuracy is 0.9778156996587031 with dt when min_samples_split = 40.

number of features in data: 3785 to calculate do: len(features_train[0])


'''
