def solution(info, edges):
    n = len(info)
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
    
    #루트에는 항상 양, 양 <= 늑대이면 모든 양 사라짐
    visited = [False] * n
    answer = -1e9
    
    def dfs(now, sheep, wolf, can_visit):
        nonlocal answer
        if sheep <= wolf:
            return
        
        answer = max(answer, sheep)
        
        for v in can_visit:
            if not visited[v]:
                visited[v] = True
                for a in graph[v]:
                    can_visit.append(a)
                dfs(v, sheep + (not info[v]), wolf + info[v], can_visit)
                for a in graph[v]:
                    can_visit.remove(a)
                visited[v] = False
        

    dfs(0, 1, 0, [*graph[0]])
    visited[0] = True
    print(answer)
    
    
    return answer