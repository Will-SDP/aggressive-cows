from distance_ok import distance_ok 
from error_codes import Error

e = Error()

def aggressive_cows(stalls, cows):
    # Sort the stalls to calculate min and max value
    stalls.sort() 

    # Get the size of the array. 
    size = len(stalls) -1 

    # Assign upper and lower index 
    min = stalls[0]
    max = stalls[size]

    # Record the highest value that works
    max_value = 0

    for i in range(min, max):
        if distance_ok(stalls, cows, i):
            max_value = i 

    # if max we have found a placement that works and max_value is stil 0 then return -1
    # Else return max value 

    if max_value == 0:
        return -1 
    else:
        return max_value        


