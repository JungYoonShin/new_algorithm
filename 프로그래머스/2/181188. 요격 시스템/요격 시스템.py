def solution(targets):
    answer = 1
    
    targets.sort(key=lambda x: x[1])
    
    now = targets[0][1]
    n = len(targets)
    for i in range(1, n):
        if now <= targets[i][0]:    
            now = targets[i][1]
            answer += 1
    
    return answer