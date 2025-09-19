import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
r, c = n, m

graph = [list(input().rstrip()) for _ in range(r)]

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'R':
            red_x, red_y = i, j
        elif graph[i][j] == 'B':
            blue_x, blue_y = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def move(x, y, dx, dy):
    count = 0
    while graph[x+dx][y+dy] != '#' and graph[x][y] != 'O':
        x += dx
        y += dy
        count += 1
        if graph[x][y] == 'O':
            break
    return x, y, count

def bfs():
    q = deque()
    q.append((red_x, red_y, blue_x, blue_y, 0))
    visited = set()
    visited.add((red_x, red_y, blue_x, blue_y))

    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth >= 10:
            continue

        for k in range(4):
            nrx, nry, rc = move(rx, ry, dx[k], dy[k])
            nbx, nby, bc = move(bx, by, dx[k], dy[k])

            if graph[nbx][nby] == 'O':
                continue
                # 빨간 공만 구멍에 들어가면 성공
            if graph[nrx][nry] == 'O':
                return 1

            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx -= dx[k]
                    nry -= dy[k]
                else:
                    nbx -= dx[k]
                    nby -= dy[k]

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, depth+1))
    return 0


print(bfs())