import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]

INF = 10**9
dist = [[[INF]*2 for _ in range(m)] for __ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dist[0][0][0] = 1

def bfs(x, y):
    q = deque([(0, 0, 0)])

    while q:
        a, b, broke = q.popleft()
        if a == n - 1 and b == m - 1:
            print(dist[a][b][broke])
            break

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0<= nx < n and 0<= ny <m:
                #빈칸
                if grid[nx][ny] == 0 and dist[nx][ny][broke] == INF:
                    dist[nx][ny][broke] = dist[a][b][broke] + 1
                    q.append((nx, ny, broke))

                #벽이고 아직 안 부숨
                elif grid[nx][ny] == 1 and broke == 0 and dist[nx][ny][1] == INF:
                    dist[nx][ny][1] = dist[a][b][0] + 1
                    q.append((nx, ny, 1))

bfs(0, 0)
if dist[n-1][m-1][0] == INF and dist[n-1][m-1][1] == INF:
    print(-1)