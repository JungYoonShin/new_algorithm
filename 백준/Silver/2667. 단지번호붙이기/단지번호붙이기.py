
n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(depth, x, y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                graph[nx][ny] = depth
                cnt += 1
                dfs(depth, nx, ny)

answer = []
depth = 2
flag = False
for i in range(n):
    for j in range(n):
        visited = [[False for _ in range(n)] for _ in range(n)]
        visited[i][j] = True
        if graph[i][j] == 1:
            cnt = 1
            dfs(depth, i, j)
            answer.append(cnt)
            depth += 1

answer.sort()
print(depth-2)
print(*answer, sep='\n')

