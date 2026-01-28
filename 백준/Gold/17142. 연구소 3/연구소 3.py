from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append((i, j))

answer = []

def find_combi(now, combi):
    if len(combi) == m:
        answer.append(combi[:])
        return
    for i in range(now, len(virus)):
        combi.append(i)
        find_combi(i + 1, combi)
        combi.pop()

find_combi(0, [])

def bfs(combi):
    dist = [[-1 for _ in range(n)] for _ in range(n)]
    q = deque([])

    for idx in combi:
        x, y = virus[idx]
        q.append((x, y))
        dist[x][y] = 0

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] != 1 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    max_time = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                if dist[i][j] == -1:
                    return None
                max_time = max(max_time, dist[i][j])

    return max_time

result = 10**9

for combi in answer:
    t = bfs(combi)
    if t is not None:
        result = min(result, t)

print(-1 if result == 10**9 else result)
