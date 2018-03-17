#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    from operator import itemgetter
    errors = abs(net_worths - predictions)**2

    data = zip(ages, net_worths, errors)
    data.sort(key=itemgetter(2), reverse=True)
    return data[9:]

    '''
    ### your code goes here
    #print("this is running !")
    for p,a,n in zip(predictions, ages, net_worth):
        e = abs(p-n)
        t= (a,n,e)
        cleaned_data.append(t)
    '''

    #return cleaned_data[limit:]
