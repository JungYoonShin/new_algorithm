import heapq
def solution(n, s, a, b, fares):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    
    for fare in fares:
        x, y, z  = fare
        graph[x].append((y, z))
        graph[y].append((x, z))
    

    def djk(start):
        q = []
        heapq.heappush(q, (0, start))
        dist = [1e9] * (n+1)
        dist[start] = 0

        while q:
            cost, u = heapq.heappop(q)

            if dist[u] < cost:
                continue

            for v, w in graph[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(q, (dist[v], v))
    
        return dist
    
    #s번에서 i번까지 동승 그리고 i번에서 최소거리로 각자집까지 이동
    min_cost = 1e9
    dist = djk(s)
    
    #합승을 안하는게 이득일 수도
    alone_a = dist[a]
    alone_b = dist[b]
    
    for i in range(1, n+1):
        together = dist[i]
        if dist[i] == 1e9:
            continue
        
        #i번에서 각자 집까지 이동(최소거리로)
        start_i = djk(i)
        dist_a = start_i[a]
        dist_b = start_i[b]
        
        min_cost = min(together+dist_a+dist_b, min_cost, alone_a+alone_b)
    
    return min_cost