import copy
def solution(n, wires):
    answer = 1e9
    def dfs(start, visited, graph):
        global cnt
        visited[start] = True
        for i in graph[start]:
            if not visited[i]:
                cnt += 1
                dfs(i, visited, graph)
        
        return cnt

    
    graph = [[] for _ in range(n + 1)]
    for wire in wires:
        a, b = wire
        graph[a].append(b)
        graph[b].append(a)
    
    #하나 연결선 제거
    for wire in wires:
        a, b = wire
        tmp = copy.deepcopy(graph)
        tmp[a].remove(b)
        tmp[b].remove(a)
        visited = [0] * (n+1)
        global cnt
        cnt = 1
        s = dfs(a, visited, tmp)
        answer = min(answer, abs((n-s) - s))
        
    return answer 