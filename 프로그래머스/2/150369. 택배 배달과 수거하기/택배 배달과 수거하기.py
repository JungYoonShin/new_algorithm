def solution(cap, n, deliveries, pickups):
    answer = 0
    
    deliveries = deliveries + [0]
    pickups = pickups + [0]
    for i in range(n-1, -1, -1):
        j = 0 
        deliveries[i] += deliveries[i+1]
        pickups[i] += pickups[i+1]
        while deliveries[i] > 0 or pickups[i] > 0:
            deliveries[i] -= cap
            pickups[i] -= cap
            j += 1
        
        answer += (j * (i+1))
    
    return answer * 2