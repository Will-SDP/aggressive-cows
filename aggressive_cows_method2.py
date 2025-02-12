from distance_ok import distance_ok 


def aggressive_cows(stalls, cows):
    # Sort the stalls to perform a binary search 
    stalls.sort() 

    # Get the size of the array. 
    size = len(stalls) - 1 
    
    # Check if cows exceeds stalls 
    if cows -1 > size:
        return -1  
    
    # Check for duplicate coordinates 
    # 
    check_dic = {}
    for i in stalls:
        if i not in check_dic.keys():
            check_dic[i] = 1 
        else:
            check_dic[i] += 1 
    if len(check_dic.keys()) != len(stalls):
        return -2            
    

    # Check for single stall 
    if size == 0:
        return -3 
    


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

