import heapq

def solution(n, paths, gates, summits):
    gate_set = set(gates)
    summit_set = set(summits)

    graph = [[] for _ in range(n + 1)]
    for a, b, cost in paths:
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    def dijkstra():
        dist = [1e9] * (n + 1)
        q = []
        
        for gate in gates:
            dist[gate] = 0
            heapq.heappush(q, (0, gate))

        while q:
            cost, v = heapq.heappop(q)

            if dist[v] < cost or v in summit_set:
                continue

            for togo, w in graph[v]:

                new_intensity = max(dist[v], w)
                if new_intensity < dist[togo]:
                    dist[togo] = new_intensity
                    heapq.heappush(q, (dist[togo], togo))

        return dist

    answer = [0, 1e9]  # [산봉우리 번호, intensity]
    
    dis = dijkstra()
    summits.sort()
    for summit in summits:
        if dis[summit] < answer[1]:
            answer = [summit, dis[summit]]
        elif dis[summit] < answer[1] and summit <=answer[0] :
            answer = [summit, dis[summit]]

    return answer
