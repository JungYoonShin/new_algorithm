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
                    dist[v] = cost + w
                    heapq.heappush(q, (dist[v], v))
    
        return dist
    
    #s번에서 i번까지 동승 그리고 i번에서 최소거리로 각자집까지 이동
    dist_s = djk(s)
    dist_a = djk(a)
    dist_b = djk(b)
    
    min_cost = 1e9
    for i in range(1, n+1):
        total = dist_s[i] + dist_a[i] + dist_b[i]
        if total < min_cost:
            min_cost = total
        
    
    return min_cost