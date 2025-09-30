import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split()) # n 세로, m 가로
graph = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            start_x, start_y = i, j
        if graph[i][j] == 'F':
            f_x, f_y = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([(start_x, start_y)])
cost = [[(1e9, 1e9) for _ in range(m)] for _ in range(n)]
cost[start_x][start_y] = (0, 0)

while q:
    x, y = q.popleft()
    garbage, near = cost[x][y]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            g, n2 = garbage, near

            if graph[nx][ny] == 'g':
                g += 1
            elif graph[nx][ny] == '.':
                flag = False
                for t in range(4):
                    tx, ty = nx + dx[t], ny + dy[t]
                    if 0 <= tx < n and 0 <= ty < m and graph[tx][ty] == 'g':
                        flag = True
                        break
                if flag:
                    n2 += 1

            if (g, n2) < cost[nx][ny]:
                cost[nx][ny] = (g, n2)
                q.append((nx, ny))

print(cost[f_x][f_y][0], cost[f_x][f_y][1])
