import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

start_x, start_y = 0, 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  q = deque([(x, y)])

  while q:
    a, b = q.popleft()
    for i in range(4):
      nx, ny = a+dx[i], b+dy[i]
      if 0<=nx<n and 0<=ny<m:
        if graph[nx][ny] == 1:
          graph[nx][ny] = graph[a][b] + 1
          q.append((nx, ny))

bfs(0, 0)
print(graph[n-1][m-1])