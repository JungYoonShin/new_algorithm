import heapq
def solution(n, paths, gates, summits):
    answer = 1e9
    result = []
    graph = [[] for _ in range(n+1)]
    summits = set(summits)
    for a, b, c in paths:
        graph[a].append([b, c])
        graph[b].append([a, c])
    
    def djk():
        q = []
        intensity = [1e9] * (n+1)
        for gate in gates:
            heapq.heappush(q, (0, gate))
            intensity[gate] = 0
            
        while q:
            dist, now = heapq.heappop(q)
            
            #산봉우리에 도착한 경우
            if now in summits:
                result.append([now, min(answer, dist)])
                continue
            
            if intensity[now] < dist:
                continue
            
            for togo, d in graph[now]:
                big = max(dist, d)
                if big < intensity[togo]:
                    intensity[togo] = big
                    heapq.heappush(q, (big, togo))
    djk()
    result.sort(key = lambda x: (x[1], x[0]))
    return result[0]