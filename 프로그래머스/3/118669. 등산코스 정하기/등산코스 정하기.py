import heapq
def solution(n, paths, gates, summits):
    answer = []
    INF = 1e9
    summit_set = set(summits)
    gates_set = set(gates)
    
    graph = [[] for _ in range(n+1)]
    for path in paths:
        a, b, cost = path
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    
    def djk(gate):
        dist = [INF] * (n+1)
        q = []
        
        for g in gate:
            heapq.heappush(q, (0, g))
            dist[g] = 0
            
        while q:
            cost, now = heapq.heappop(q)
            if dist[now] < cost or now in summit_set:
                continue
                
            for togo, distance in graph[now]:
                if togo in gates_set:
                    continue
                new_intensity = max(dist[now], distance)
                if new_intensity < dist[togo]:
                    dist[togo] = new_intensity
                    heapq.heappush(q, (dist[togo], togo))
                    
        return dist
    
    dis = djk(gates)
    answer = [0, 1e9]  # [산봉우리 번호, intensity]
    
    for summit in summits:
        if dis[summit] < answer[1]:
            answer = [summit, dis[summit]]
        elif dis[summit] == answer[1] and summit < answer[0]:
            answer = [summit, dis[summit]]
    
    
    
    
    
    return answer