
def distance_ok(stalls, cows, distance):
    cows_placed = 1 
    prev = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - prev >= distance:
            prev = stalls[i]
            cows_placed += 1 

            # If we have already placed enough cows there is no need to
            # continue the evaluation so return True
            if cows_placed >= cows:
                return True
    return cows_placed >= cows 



