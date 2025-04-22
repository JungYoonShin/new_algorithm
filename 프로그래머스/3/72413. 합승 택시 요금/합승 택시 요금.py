from heapq import heappop, heappush

def solution(n, s, a, b, fares):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        c, d, f = fare
        graph[c].append((d, f))
        graph[d].append((c, f))
    
    def dijkstra(now):
        nonlocal graph
        dist = [1e9] * (n+1)
        
        dist[now] = 0
        
        #우선순위 큐에 (거리 0, 첫 정점)만 먼저 넣는다.
        q = [[0, now]]
        
        while q:
            now_dist, x = heappop(q)
            
            if dist[x] < now_dist:
                continue
            
            for next_node, next_dist in graph[x]:
                if dist[next_node] > now_dist + next_dist:
                    dist[next_node] = now_dist + next_dist
                    heappush(q, (now_dist + next_dist, next_node))
        return dist
    
    
    #특정 노드에서 시작해서 모든 정점으로의 이동거리 
    D = [0] + [dijkstra(i) for i in range(1, n+1)]
    
    answer = 1e9
    for i in range(1, n+1):
        answer = min(answer, D[s][i] + D[i][a] + D[i][b])
                   
        
    return answer