#가로 m, 세로 n, 가장 테두리는 모두 막혀 있음
#게임 목표는 빨간 구슬을 구멍으로 빼내기, 파란 구슬이 들어가면 안됨
#두 구슬 동시에 같은 칸 불가, 빨간 공만 빼내야함
#더 이상 구슬이 움직이지 않을 때까지 기울임

from collections import deque

n, m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            rx, ry = i, j
        if graph[i][j] == 'B':
            bx, by = i, j



def move(x, y, d):
    move = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]

        if graph[nx][ny] == '#':
            return [x, y, move, False]

        move += 1
        if graph[nx][ny] == 'O':
            return [nx, ny, move, True]
        x, y = nx, ny

answer = False

def game():
    global answer
    q = deque([(rx, ry, bx, by,0)])
    visited = set()
    visited.add((rx, ry, bx, by))

    while q:
        crx, cry, cbx, cby, cnt = q.popleft()

        if cnt >= 10:
            continue

        for i in range(4):
            nrx, nry, move_r, flagR = move(crx, cry, i)
            nbx, nby, move_b, flagB = move(cbx, cby, i)

            if flagB:
                continue

            if flagR:
                return cnt+1

            if nrx == nbx and nry == nby:
                if move_r > move_b:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, cnt + 1))

    return -1

print(game())