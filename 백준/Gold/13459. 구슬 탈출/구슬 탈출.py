import sys
input = sys.stdin.readline
from collections import deque


#파란 구슬을 구멍에 넣지 않으면서 빨간 구슬을 10번 이하로 움직여서 빼낼 수 있으면 1
n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def move(d, x, y):
    cnt = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if board[nx][ny] == '#':  # 벽이면 멈춤
            break
        if board[nx][ny] == 'O':  # 구멍이면 좌표만 반환
            return nx, ny, cnt
        x, y = nx, ny
        cnt += 1
    return x, y, cnt

def bfs(a, b, c, d, cnts):
    q = deque([(a, b, c, d, cnts)])
    visited = set()
    visited.add((a, b, c, d))

    while q:
        rx, ry, bx, by, cnt = q.popleft()

        if cnt >= 11:
            return 0

        for d in range(4):
            nrx, nry, depthr = move(d, rx, ry)
            nbx, nby, depthb = move(d, bx, by)

            if board[nbx][nby] == 'O':
                continue

            if board[nrx][nry] == 'O':
                return 1

            #둘이 같은 칸에 못있게 함
            if (nrx == nbx) and (nry == nby):
                if depthr > depthb:
                    nrx -= dx[d]
                    nry -= dy[d]
                else:
                    nbx -= dx[d]
                    nby -= dy[d]

            if board[nrx][nry] != 'O' and board[nbx][nby] != 'O':
                if (nrx, nry, nbx, nby) not in visited:
                    visited.add((nrx, nry, nbx, nby))
                    q.append((nrx, nry, nbx, nby, cnt+1))

    return 0

print(bfs(rx, ry, bx, by, 1))