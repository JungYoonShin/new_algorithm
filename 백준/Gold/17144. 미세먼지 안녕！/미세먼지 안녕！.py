# 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
#1. (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
#2.  인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
#3. 확산되는 양은 Ar,c/5이고 소수점은 버린다. 즉, ⌊Ar,c/5⌋이다.
#4. (r, c)에 남은 미세먼지의 양은 Ar,c - ⌊Ar,c/5⌋×(확산된 방향의 개수) 이다.

# 공기청정기가 작동한다.
# 1. 공기청정기에서는 바람이 나온다.
# 2. 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
# 3. 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
# 4. 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.

from collections import deque
r, c, t = map(int, input().split()) #행, 열, 초
graph = [list(map(int, input().split())) for _ in range(r)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

machine = []

for i in range(r):
    for j in range(c):
        if graph[i][j] == -1:
            machine.append([i, j])

#미세먼지 확산
def bfs():
    q = deque([])
    new = [row[:] for row in graph]

    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0<=nx<r and 0<=ny<c:
                if graph[nx][ny] != -1:
                    new[nx][ny] += graph[x][y] // 5
                    new[x][y] -= (graph[x][y] // 5)
    return new

def dfs(x, y, graph, flag):
    d = 0
    a, b = x + dx[d], y+ dy[d]
    new = [row[:] for row in graph]
    new[a][b] = 0
    while True:
        if not(0<=a + dx[d]<r and 0<=b + dy[d]<c):
            if flag: d = (d+1) % 4
            else: d = (d-1) % 4
        else:
            nx, ny = a+dx[d], b+dy[d]
            if nx == x and ny == y:
                break
            new[nx][ny] = graph[a][b]
            a, b = nx, ny
    return new

for _ in range(t):
    new = bfs()

    #위쪽 이동
    top_x, top_y = machine[0]
    move_top = dfs(top_x, top_y, new, True)

    bottom_x, bottom_y = machine[1]
    move_bottom = dfs(bottom_x, bottom_y, move_top, False)
    graph = move_bottom


dust = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            dust += graph[i][j]

print(dust)