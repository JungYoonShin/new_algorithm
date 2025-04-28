from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

def dj(start):
    dist = [1e9] * (n + 1)
    dist[start] = 0

    q = [[0, start]]

    while q:
        now_dist, now_node = heappop(q)

        if dist[now_node] < now_dist:
            continue

        for next_node, next_cost in graph[now_node]:
            if dist[next_node] > next_cost + now_dist:
                dist[next_node] = now_dist + next_cost
                heappush(q, (now_dist + next_cost, next_node))
    return dist


answer = dj(1)
print(answer[n])

