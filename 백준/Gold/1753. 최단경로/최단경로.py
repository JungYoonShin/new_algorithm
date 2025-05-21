import sys
import heapq
input=sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
k = int(input())  #시작정점

for _ in range(E):
    u, v, e = map(int, input().split())
    graph[u].append((v, e))

cost = [1e9 for _ in range(V+1)]

visited = [False] * (v+1)

def dijkstra(start):
    global cost
    q = []
    heapq.heappush(q, (0, start))
    cost[k] = 0

    while q:
        dist, now = heapq.heappop(q)
        if cost[now] < dist:
            continue

        for i in graph[now]:
            if i[1] + dist < cost[i[0]]:
                cost[i[0]] = i[1] + dist
                heapq.heappush(q, (i[1]+ dist, i[0]))


dijkstra(k)
for i in range(1, V+1):
    if cost[i] == 1e9:
        print("INF")
    else:
        print(cost[i])