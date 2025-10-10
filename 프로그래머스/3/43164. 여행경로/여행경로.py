from collections import defaultdict
def solution(tickets):
    answer = ["ICN"]
    n = len(tickets)
    graph = defaultdict(list)
    for i, ticket in enumerate(tickets):
        start, end = ticket
        graph[start].append([end, i])
    
    for k in graph.keys():
        graph[k].sort()
        
    visited = defaultdict(bool)
    def dfs(now):
        
        if len(answer) == (n+1):
            print(answer)
            return answer
        
        if not graph[answer[-1]] and len(answer) != n+1:
            return False
        
        for v in graph[now]:
            if not visited[v[1]]:
                visited[v[1]] = True
                answer.append(v[0])
                result = dfs(v[0])
                if result:
                    return result
                visited[v[1]] = False
                answer.pop()
                    
            
    return dfs("ICN")
