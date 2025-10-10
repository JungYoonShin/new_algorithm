import heapq
def solution(N, road, K):
    answer = 0
    n = N
    #1번 마을에 있는 음식점이 K 이하의 시간에 배달이 가능한 마을의 개수를 return
    graph = [[] for _ in range(n+1)]
    
    for a, b, c in road:
        graph[a].append([b, c])   #이어진 노드, 가중치
        graph[b].append([a, c])
    
    def djk():
        q = []
        heapq.heappush(q, [0, 1])  #cost, 현재 노드
        dist = [1e9] * (n+1)
        dist[1] = 0
        
        while q:
            cost, now = heapq.heappop(q)
            
            if dist[now] < cost:
                continue
            
            for v in graph[now]:
                if dist[now] + v[1] < dist[v[0]]:
                    dist[v[0]] = dist[now] + v[1]
                    heapq.heappush(q, [dist[v[0]], v[0]])
        return dist
    
    result = djk()
    for i, v in enumerate(result):
        if v <= K:
            answer += 1

    return answer