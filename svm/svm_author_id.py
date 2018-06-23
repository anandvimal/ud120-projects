#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
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

import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score



#make data smaller:
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]


#clf = SVC(kernel='linear')

#chaning kernel to rbf
#clf = SVC(kernel = 'rbf')

#trying different values of c:
#clf = SVC(kernel = 'rbf', C = 10)
#clf = SVC(kernel = 'rbf', C = 100)
#clf = SVC(kernel = 'rbf', C = 1000)
clf = SVC(kernel = 'rbf', C = 10000)
#clf = SVC(kernel = 'rbf', C = 100000)
'''
C = 10 , acuracy = 0.6160409556313993
C = 100, acuracy = 0.6160409556313993
C= 1000, acuracy = 0.8213879408418657
C= 10000 acuracy = 0.8924914675767918
C= 100000 acuracy= 0.8600682593856656 #not in course just did.
on full data with C=10k and kernel=rbf we got 0.9908987485779295 as accuracy_score
'''


"""
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
"""

t0 = time()
clf.fit(features_train, labels_train)
training_time = round(time()-t0, 3)


t0 = time()
y_pred = clf.predict(features_test)
prediction_time = round(time()-t0, 3)


t0 = time()
acc = accuracy_score(labels_test, y_pred)
accuracy_time = round(time()-t0, 3)

print("accuracy_score is :", acc)

print("training time:", training_time)
print("prediction_time", prediction_time)
print("accuracy_time",accuracy_time)


#0 or 1, corresponding to Sara and Chris respectively
print("10:",y_pred[10])
print("26:",y_pred[26])
print("50:",y_pred[50])

#########################################################
