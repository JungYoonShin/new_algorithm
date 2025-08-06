import sys
from collections import deque
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
bus = [list(map(int, input().split())) for _ in range(m)]
start, end = map(int, input().split())

graph = [[] for _ in range(n+1)]
answer = [1e9] * (n+1)

def dijkstra():
    q = []
    heapq.heappush(q, (0, start))
    answer[start] = 0

    while q:
        cost, now = heapq.heappop(q)
        if answer[now] < cost:
            continue

        for v in graph[now]:
            if answer[v[0]] > answer[now] + v[1]:
                answer[v[0]] = answer[now] + v[1]
                heapq.heappush(q, (answer[v[0]], v[0]))

for b in bus:
    s, e, c = b
    graph[s].append((e, c))

dijkstra()
print(answer[end])