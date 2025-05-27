import sys
from collections import deque
input=sys.stdin.readline

n = int(input())
status = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if status[i][j] == 9:
            shark_x, shark_y = i, j
            status[i][j] = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

shark = 2
def bfs(x, y):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    q = deque([(x, y, 0)])
    visited[x][y]=1
    fish = []

    while q:
        a, b, c = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny] and shark >= status[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny, c+1))
                    if shark > status[nx][ny] > 0:
                        fish.append((c+1, nx, ny))

    fish.sort()
    return fish

time = 0
cnt = 0
while True:
    fish = bfs(shark_x, shark_y)
    if len(fish) == 0:
        break

    dist, x, y = fish[0]
    cnt += 1
    time += dist

    if shark == cnt:
        cnt = 0
        shark += 1

    status[x][y] = 0
    shark_x, shark_y = x, y


print(time)