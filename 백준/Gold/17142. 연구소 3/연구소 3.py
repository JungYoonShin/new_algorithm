import sys
from collections import deque
from itertools import combinations as c
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

INF = 100000

def bfs(q, blank_cnt):
  time=0
  visited = [[False] * n for _ in range(n)]

  while True:
    length = len(q)
    if blank_cnt == 0:
        return time
    # 바이러스가 복제 X
    elif length == 0:
        return INF

    time += 1

    for _ in range(length):
      x, y = q.popleft()
      visited[x][y] = 1

      for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < n and 0 <= new_y < n and not visited[new_x][new_y]:
          if not visited[new_x][new_y] and graph[new_x][new_y] == 0:
            q.append([new_x, new_y])
            blank_cnt -= 1
            visited[new_x][new_y] = 1

          if not visited[new_x][new_y] and graph[new_x][new_y] == 2:
            q.append([new_x, new_y])
            visited[new_x][new_y] = 1
virus_location = []
blank_cnt=0
for i in range(n):
  for j in range(n):
    if graph[i][j] == 0:
      blank_cnt += 1
    if graph[i][j] == 2:
      virus_location.append((i, j))


virus_list = c(virus_location, m)

result = INF
for virus_combo in virus_list:
  q = deque()
  for virus in virus_combo:
    q.append(virus)

  time = bfs(q, blank_cnt)
  result = min(result, time)

if result == INF:
  print(-1)
else:
  print(result)

