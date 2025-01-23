from distance_ok import distance_ok 

error_codes = {
    -1: 'Cows exceeds stalls.',
    -2: 'Duplicate stall coordinates have been input.',
    -3: 'Unable to calculate distance with a single stall', 
    -4: 'Negative stall coordinates are not permitted.'

}

def aggressive_cows(stalls, cows):
    # Sort the stalls to perform a binary search 
    stalls.sort() 

    # Get the size of the array. 
    size = len(stalls) - 1 

    # Assign upper and lower index 
    lower_idx = stalls[0]
    upper_idx = stalls[size]

    while lower_idx <= upper_idx:
        mid_point = (lower_idx + upper_idx) // 2 

        if distance_ok(stalls, cows, mid_point):
            lower_idx = mid_point + 1
        else:
            upper_idx = mid_point - 1 
    return upper_idx            

