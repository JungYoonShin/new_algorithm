import sys
input = sys.stdin.readline

n,m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

cnt = 1
# 북동남서(0, 1, 2, 3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited[r][c] = 1

while True:
  flag = 0
  for _ in range(4):
    d = (d+3)%4
    x = r + dx[d]
    y = c + dy[d]
    if 0 <= x < n and 0 <= y < m and graph[x][y] == 0:
      if visited[x][y] == 0:
        visited[x][y] = 1
        cnt += 1
        flag = 1
        r, c = x, y
        break
  if flag == 0:
    if graph[r-dx[d]][c-dy[d]] == 1:
      print(cnt)
      break
    else:
      r = r - dx[d]
      c = c - dy[d]
  