import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    visited = [[0 for _ in range(m)] for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y):
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    dfs(nx, ny)

    result = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 1:
                dfs(i, j)
                result += 1
    print(result)