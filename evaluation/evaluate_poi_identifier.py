#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here
### it's all yours from here forward!
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split( features, labels, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier(random_state=0)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("accuracy on test dataset is: ", accuracy)

#quiz 28 ch15
print('total pois : ',sum(y_test))

#quiz 29 ch15
print('number of people in test set : ',len(y_test))

'''
for quiz 30
acuuracy = 25/29 = .84
'''


true_positives_count = 0
for i in range(len(y_pred)):
    if (y_pred[i] == 1 ) and (y_test == 1) :
        true_positives_count = true_positives_count + 1

print('Number of true positives : ', true_positives_count)


#calculate precission score #q32
from sklearn.metrics import precision_score
precision_score1 = precision_score(y_test, y_pred, average='binary')
print("precision_score : ", precision_score1)


#calculate recall score #q33
from sklearn.metrics import recall_score
recall_score1 =  recall_score(y_test, y_pred, average='binary')
print("recall_score : ", recall_score1)

#sample data
#import numpy as np
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

#a = np.array([1, 2], dtype=np.float32)

y_pred =  predictions
y_test =  true_labels

precision_score2 = precision_score(y_test, y_pred, average='binary')
print("precision_score on sample data : ", precision_score2)

recall_score2 =  recall_score(y_test, y_pred, average='binary')
print("recall_score on sample data : ", recall_score2)
