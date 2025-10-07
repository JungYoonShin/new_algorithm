import heapq
def solution(n, s, a, b, fares):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        c, d, f = fare
        graph[c].append([d, f])
        graph[d].append([c, f])
        
    
    def djk(start):
        q = []
        heapq.heappush(q, (0, start))
        dist = [1e9] * (n+1)
        dist[start] = 0
        
        while q:
            cost, now = heapq.heappop(q)
            
            if dist[now] < cost:
                continue
            
            for v in graph[now]:
                if cost + v[1] < dist[v[0]]:
                    dist[v[0]] = dist[now] + v[1]
                    heapq.heappush(q, (dist[v[0]], v[0]))
        return dist
    
    #s에서 각 지점까지의 최단거리를 구한다.
    dist_s = djk(s)
    alone_a = dist_s[a]
    alone_b = dist_s[b]
    
    answer = alone_a + alone_b
    
    for i in range(1, n+1):
        together = dist_s[i]
        alone = djk(i)
        total = together + alone[a] + alone[b]
        answer = min(answer, total)
    
    return answer