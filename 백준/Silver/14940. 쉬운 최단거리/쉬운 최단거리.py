import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

#0은 갈 수 없는 땅, 1은 갈 수 있는 땅, 2는 목표지점
#모든 지점에 대해서 목표지점까지의 거리
#원래 갈 수 없는 땅인 위치는 0을 출력, 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            startx, starty = i, j

visited = [[False for _ in range(m)] for _ in range(n)]
cost = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(startx, starty):
    q = deque([(startx, starty, 0)])
    visited[startx][starty] = True
    cost[startx][starty] = 0

    while q:
        a, b, depth = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    cost[nx][ny] = depth+1
                    visited[nx][ny] = True
                    q.append((nx, ny, depth + 1))

bfs(startx, starty)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and cost[i][j]==0:
            cost[i][j] = -1

for x in cost:
    print(*x, end="\n")

