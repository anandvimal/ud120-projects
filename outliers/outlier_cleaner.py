#!/usr/bin/python
import operator

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    # predictions : is a list of predicted targets that come from your regression,
    # ages : is the list of ages in the training set, and
    # net_worths : is the actual value of the net worths in the training set

    '''
    There should be 90 elements in each of these lists
    (because the training set has 90 points in it).
    Your job is to return a list called cleaned_data that has only 81 elements
    in it, which are the 81 training points where the predictions and
    the actual values (net_worths) have the smallest errors (90 * 0.9 = 81).
    The format of cleaned_data should be a list of tuples,
    where each tuple has the form (age, net_worth, error).
    '''



    cleaned_data = []
    new_data = []
    ### your code goes here
    print("****************")

    for i in range( len(predictions) ):
        #print('print : ',predictions[i], ages[i], net_worths[i])
        error = abs(predictions[i] - net_worths[i])
        data_cell = ( float(ages[i]), float(net_worths[i]), float(error) )
        new_data.append(data_cell)
        #mean_squared_error(diabetes_y_test, diabetes_y_pred)
    #print (new_data)

    '''
    for i in new_data:
        print i
    '''

    new_data.sort(key=operator.itemgetter(2))



    cleaned_data = new_data[0:81]

    print("****************")

    return cleaned_data
