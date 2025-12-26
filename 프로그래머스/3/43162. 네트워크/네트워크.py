def solution(n, computers):
    answer = 0
    visited = [0] * n
    graph = [[] for _ in range(n)]
        
    def dfs(v):
        visited[v] = True
        for i in range(n):
            if i != n and computers[v][i] == 1:
                if not visited[i]:
                    dfs(i)
        
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
        
    return answer