#바이러스는 상하좌우로 퍼져나간다. 벽을 꼭 3개를 세워야 한다.
#0 -> 빈칸, 1 -> 벽, 2 -> 바이러스
#얻을 수 있는 안전 영역 크기의 최댓값

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = []
from collections import deque
def bfs():
    q = deque([])
    for i in range(n):
        for j in range(m):
            if new[i][j] == 2:
                q.append([i, j])
                new[i][j] = 3

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0<=nx<n and 0<=ny<m:
                if new[nx][ny] == 0:
                    new[nx][ny] = 2
                    q.append([nx, ny])


# 조합 구하기(라이브러리 사용안하고 구현해보기)
def find_combi(now, combi):
    if len(combi) == 3:
        answer.append(combi[:])
        return

    for i in range(now, n*m):
        if graph[i//m][i%m] == 0:
            combi.append(i)
            find_combi(i+1, combi)
            combi.pop()

find_combi(0, [])

result = -1e9
for combi in answer:
    new = [row[:] for row in graph]
    for idx in combi:
        new[idx // m][idx % m] = 1

    bfs()
    sum = 0
    for i in range(n):
        for j in range(m):
            if new[i][j] == 0:
                sum += 1

    result = max(result, sum)
print(result)

