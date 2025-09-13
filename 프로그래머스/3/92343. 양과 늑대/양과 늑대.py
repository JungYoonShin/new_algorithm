def solution(info, edges):
    answer = 0
    
    def dfs(sheep, wolf):
        nonlocal answer
        if sheep > wolf:
            answer = max(answer, sheep)
        else:
            return
        
        for a, b in edges:
            if visited[a] and not visited[b]:
                visited[b] = 1
                if info[b] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                
                visited[b] = 0
    visited = [False] * len(info)
    visited[0] = True
    dfs(1, 0)
    return answer