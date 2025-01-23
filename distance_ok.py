
def distance_ok(stalls, cows, distance):
    cows_placed = 1 
    prev = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - prev >= distance:
            prev = stalls[i]
            cows_placed += 1 
    return cows_placed >= cows 



