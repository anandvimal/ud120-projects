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

print( len(enron_data) )

total_features = 0
total_poi = 0
total_salary_people = 0
for i in enron_data:
    #print(i)
    #if(enron_data[i]["poi"]==True):
    if( enron_data[i]['salary'] != 'NaN' ):
        total_salary_people = total_salary_people+1
    else:
        print("without salary:",i)


print("total total_salary_people: ", total_salary_people)
        #print("True")
        #total_poi += 1
    #print( (enron_data[i]))
    #print( total_salary_people )
    #print("total poi: ",total_poi)

    #print("\n\n")

    #total_features = total_features + len(i)
    #print(len(i))

#print(enron_data['PRENTICE JAMES'])
#print(enron_data['COLWELL WESLEY'])
#print(enron_data['SKILLING JEFFREY K'])

#print("total features: ", total_features)
#print("each features: ", total_features/146.0)
print("\n\n\n\n")
total_email = 0

for i in enron_data:
    #print('\n')
    if( enron_data[i]['email_address'] != 'NaN'):
        total_email = total_email+1
    print(enron_data[i]['email_address'])


print("total emails: ",total_email)

total_payments = 0
total = 0
for i in enron_data:
    total +=1
    print(enron_data[i]['total_payments'])
    if(enron_data[i]['total_payments'] != 'NaN'):
        total_payments += 1

print("total payments: ", total_payments)
print("total: ",total)

total_poi = 0
nan_and_poi = 0

for i in enron_data:
    #print(enron_data[i])
    if(enron_data[i]["poi"]==True):
        print(enron_data[i]["poi"])
        total_poi +=1
        if(enron_data[i]['total_payments'] == 'NaN'):
            nan_and_poi +=1


print("total poi:", total_poi)
print("total payment is not nan and is poi: ",nan_and_poi)
