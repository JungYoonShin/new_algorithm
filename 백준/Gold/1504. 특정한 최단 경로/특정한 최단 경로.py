import sys
import heapq

input = sys.stdin.readline

#1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])   #노드, 가중치
    graph[b].append([a, c])

v1, v2 = map(int, input().split())

def djk(start):
    q = []
    heapq.heappush(q, [0, start]) #가중치, 시작 노드
    dist = [1e9] * (n+1)
    dist[start] = 0

    while q:
        cost, now = heapq.heappop(q)

        if dist[now] < cost:
            continue

        for v in graph[now]:
            if dist[now] + v[1] < dist[v[0]]:
                dist[v[0]] = dist[now] + v[1]
                heapq.heappush(q, [dist[v[0]], v[0]])
    return dist

start1 = djk(1)
v1_v2 = djk(v1) #v1에서 v2 최단거리
start4 = djk(n) #n에서 a, b 노드 까지의 최단거리
# 1 -> v1 -> v2 -> N인 경우
version1 = start1[v1] + v1_v2[v2] + start4[v2]
# 1 -> v2 -> v1 -> N인 경우
version2 = start1[v2] + v1_v2[v2] + start4[v1]

answer = min(version1, version2)

if answer >= 1e9:
    print(-1)
else:
    print(answer)