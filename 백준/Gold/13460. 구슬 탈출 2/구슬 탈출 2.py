#백준

from collections import deque
n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            rx, ry = i, j
        if graph[i][j] == 'B':
            bx, by = i, j

q = deque([(rx, ry, bx, by, 1)])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = set()

def moves(x, y, d):
    cnt = 0
    while True:
        cnt += 1
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:   # 여기 m은 전체 열 크기
            if graph[nx][ny] == '#':
                return x, y, cnt-1
            x, y = nx, ny
            if graph[nx][ny] == 'O':
                return x, y, cnt


while q:
    r_x, r_y, b_x, b_y, move = q.popleft()

    if move > 10:
        print(-1)
        exit()

    for d in range(4):

        nrx, nry, move_r = moves(r_x, r_y, d)
        nbx, nby, move_b = moves(b_x, b_y, d)

        if graph[nbx][nby] == 'O':
            continue

        if graph[nrx][nry] == 'O':
            print(move)
            exit()

        if (nrx, nry) == (nbx, nby):
            if move_r < move_b:
                nbx -= dx[d]
                nby -= dy[d]
            else:
                nrx -= dx[d]
                nry -= dy[d]

        if (nrx, nry, nbx, nby) not in visited:
            visited.add((nrx, nry, nbx, nby))
            q.append((nrx, nry, nbx, nby, move+1))

print(-1)




