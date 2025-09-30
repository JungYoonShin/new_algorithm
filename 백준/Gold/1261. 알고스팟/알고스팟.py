import sys

input = sys.stdin.readline
import heapq


n, m = map(int, input().split()) #가로가 N, 세로가 M
graph = [list(map(int, input().rstrip())) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cost = [[1e9 for _ in range(n)] for _ in range(m)]
q = []
cost[0][0] = 0
heapq.heappush(q, (0, 0, 0))

while q:
    wall, a, b = heapq.heappop(q)

    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if wall + graph[nx][ny] < cost[nx][ny]:
                cost[nx][ny] = wall + graph[nx][ny]
                heapq.heappush(q, (cost[nx][ny], nx, ny))

print(cost[m-1][n-1])