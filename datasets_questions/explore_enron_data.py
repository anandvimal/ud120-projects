#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#How many data points (people) are in the dataset?
print("total number of people: ",len(enron_data))

#for each person how many people are available
print("no of features for each person",len(enron_data["SKILLING JEFFREY K"]))


#data[person_name]["poi"]==1
count_poi = 0
for i in enron_data:
    if enron_data[i]["poi"] == 1:
        count_poi += 1

print("total poi in enron data: ",count_poi)
#('total poi in enron data: ', 18)


#total value of stock for james prentice.
print("total value of stock of James Prentice", enron_data['PRENTICE JAMES']['total_stock_value'])

# 19 How many email messages do we have from Wesley Colwell to persons of interest?
print(" WESLEY COLWELL \n", enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

# 20 VALUE OF STOCK OPTION Exercised by JEFFREY k SKILLING
print("value of stock options exercised by Jeffrey K Skilling", enron_data['SKILLING JEFFREY K']['exercised_stock_options'])



#end of file
