def solution(n, computers):
    answer = 0
    
    visited = [0] * len(computers)
    
    def dfs(i):
        for i, connect in enumerate(computers[i]):
            if not visited[i] and connect:
                visited[i] = True
                dfs(i)

    for i, computer in enumerate(computers):
        if not visited[i]:
            visited[i] = True
            answer += 1
            dfs(i)
        
    return answer