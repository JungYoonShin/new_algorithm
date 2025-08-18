from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)   
    waiting = deque(truck_weights)        
    cur_weight = 0                         

    while bridge:
        time += 1
        cur_weight -= bridge.popleft()

        if waiting:
            if cur_weight + waiting[0] <= weight:
                w = waiting.popleft()
                bridge.append(w)
                cur_weight += w
            else:
                bridge.append(0)


    return time
