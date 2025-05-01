import sys
from collections import deque

input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(5)]
start_x, start_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False for _ in range(5)] for _ in range(5)]
dist = [[0 for _ in range(5)] for _ in range(5)]

#학생이 현재 위치 (r, c)에서 시작하여 1이 적혀 있는 칸에 도착하기 위한 최소 이동 횟수를 출력하자. 현
def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        a, b = q.popleft()


        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0<=nx<5 and 0<=ny<5:
                if not visited[nx][ny] and graph[nx][ny] != -1:
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[a][b] + 1
                    q.append((nx, ny))
                    if graph[nx][ny] == 1:
                        return dist[nx][ny]
    return -1

print(bfs(start_x, start_y))


