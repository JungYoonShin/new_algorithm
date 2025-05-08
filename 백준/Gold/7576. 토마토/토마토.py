import sys
from collections import deque
input=sys.stdin.readline

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append([i, j])

def bfs():
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b

            if 0<=nx<n and 0<=ny<m:
                if tomato[nx][ny] == 0:
                    tomato[nx][ny] = tomato[a][b] + 1
                    q.append((nx, ny))


bfs()
result = 0
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    else:
        result = max(result, max(i))

print(result-1)
