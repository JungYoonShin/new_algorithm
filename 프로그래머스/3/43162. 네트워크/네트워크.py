def solution(n, computers):
    answer = 0
    
    def dfs(x):
        visited[x] = True
        
        for i in range(n):
            if computers[x][i] and not visited[i]:
                dfs(i)
    
    visited = [0] * n
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer