def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    visited = [False] * n
    
    def explore(visit, left):   
        nonlocal answer
        for i in range(n):
            if not visited[i] and left >= dungeons[i][0]:
                visited[i] = True
                visit.append(i)
                explore(visit, left-dungeons[i][1])
                visit.pop()
                visited[i] = False
        
        if answer < len(visit):
            answer = len(visit)
    
    explore([], k)
        
    return answer