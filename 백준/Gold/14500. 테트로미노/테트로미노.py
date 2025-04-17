import sys

input = sys.stdin.readline

n, m = map(int, input().split()) #세로, 가로

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_result = -1e9

# 'ㅜ'를 제외한 도형 (dfs)
def dfs(x, y, visited, cnt, s):
    global max_result

    if cnt == 4:
        max_result = max(max_result, s)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, visited, cnt+1, s + graph[nx][ny])
                visited[nx][ny] = False

for i in range(n):
    for j in range(m):
        answer = []
        visited[i][j] = True
        dfs(i, j, visited, 1, graph[i][j])
        visited[i][j] = False

# 'ㅜ' 도형(완전탐색)
d = [[(0, 1), (0, 2), (1, 1)],
    [(0, 1), (0, 2), (-1, 1)],
    [(1, 0), (2, 0), (1, 1)],
    [(1, 0), (2, 0), (1, -1)]]
for i in range(n):
    for j in range(m):
        for k in d:
            can = []
            can.append(graph[i][j])
            for d_x, d_y in k:
                nx = i + d_x
                ny = j + d_y

                if 0<=nx<n and 0<=ny<m:
                    can.append(graph[nx][ny])
            max_result = max(max_result, sum(can))
print(max_result)