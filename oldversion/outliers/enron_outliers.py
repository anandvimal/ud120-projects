#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

salary_data = {}
for i in data_dict:
    print i
    if data_dict[i]['salary'] != 'NaN':
        if data_dict[i]['bonus'] != 'NaN':
            salary_data[i] = data_dict[i]['salary'] + data_dict[i]['bonus']

import operator

sorted_x = sorted(data_dict.items(), key=operator.itemgetter(0))
print "\n\n",sorted_x
print "\n\n\n"

for i in sorted_x:
    print i[1]['bonus']

#for i in data_dict:
    #print data_dict[i]['salary'],"  ",data_dict[i]['bonus']
