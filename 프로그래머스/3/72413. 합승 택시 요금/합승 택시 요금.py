import heapq
def solution(n, s, a, b, fares):
    INF = 1e9
    
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        graph[fare[0]].append([fare[1], fare[2]])
        graph[fare[1]].append([fare[0], fare[2]])
        
        
    def djk(start):
        dist = [INF] * (n+1)
        dist[start] = 0
        q = []
        heapq.heappush(q, (0, start))
        
        while q:
            cost, v = heapq.heappop(q)
            if dist[v] < cost:
                continue
            
            for togo, w in graph[v]:
                if dist[v] + w < dist[togo]:
                    dist[togo] = dist[v] + w
                    heapq.heappush(q, [dist[togo], togo])
        return dist

    
    together = djk(s)
    alone_a = together[a]
    alone_b = together[b]
    
    answer = alone_a + alone_b
    for i in range(1, n+1):
        #i까지 합승을 하는 거임, 합승을 안할 수도 잇음..(각자 가는게 더 빠르다면)
        alone = djk(i)
        total = together[i] + alone[a] + alone[b]
        answer = min(total, answer)
                
    return answer