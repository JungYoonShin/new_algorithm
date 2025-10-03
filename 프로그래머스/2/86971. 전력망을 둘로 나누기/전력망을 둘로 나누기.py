def solution(n, wires):
    answer = 1e9
    
    def dfs(x, not_a, not_b):
        visited[x] = True
        visit_set.add(x)
        for v in graph[x]:
            if (x == not_a and v == not_b) or (x == not_b and v == not_a):
                continue
            if not visited[v]:
                dfs(v, not_a, not_b)
    
    graph = [[] for _ in range(n+1)]
    for wire in wires:
        a, b = wire
        graph[a].append(b)
        graph[b].append(a)
    
    for wire in wires:
        visited = [False] * (n+1)
        visit_set = set()
        dfs(1, wire[0], wire[1])
        answer = min(answer, abs(len(visit_set) - (n - len(visit_set))))
        
    
    return answer