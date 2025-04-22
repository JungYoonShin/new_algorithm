import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

def dijkstra(start):
    dist = [1e9] * (n+1)
    dist[start] = 0

    # 우선순위 큐에 (거리 0, 첫 정점)만 먼저 넣는다.
    q = [[0, start]]

    while q:
        now_dist, now_node = heappop(q)

        if dist[now_node] < now_dist:
            continue

        for next_node, next_cost in graph[now_node]:
            if dist[next_node] > now_dist + next_cost:
                dist[next_node] = now_dist + next_cost
                heappush(q, (now_dist + next_cost, next_node))

    return dist


D = [0] + [dijkstra(i) for i in range(1, n+1)]
answer = -1e9
for i in range(1, n+1):
    if i!=x:
        answer = max(answer, D[i][x] + D[x][i])

print(answer)