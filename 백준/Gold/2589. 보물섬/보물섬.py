import sys
from collections import deque
input = sys.stdin.readline
L, W = map(int, input().split())

island = [list(input().rstrip()) for _ in range(L)]
land = []
for i in range(L):
    for j in range(W):
        if island[i][j] == 'L':
            land.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited, dist):
    q = deque([(x, y, 0)])
    visited[x][y] = 1

    while q:
        a, b, d = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<L and 0<=ny<W:
                if not visited[nx][ny] and island[nx][ny] == 'L':
                    visited[nx][ny] = 1
                    q.append((nx, ny, d+1))
    return d

result = -1e9
for l in land:
    visited = [[0 for _ in range(W)] for _ in range(L)]
    dist = bfs(l[0], l[1], visited, 0)
    result = max(dist, result)

print(result)