def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    
    def dfs(v):
        visited[v] = True
        for i in range(n):
            if computers[v][i] and not visited[i]:
                dfs(i)
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)

    return answer