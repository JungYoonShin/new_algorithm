import sys
from itertools import combinations
import copy

input = sys.stdin.readline

n, m = map(int, input().split()) #n이 세로, 가로 m
graph = [list(map(int, input().split())) for _ in range(n)]



empty = []

#벽을 세워야 함 ..(3개)
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty.append((i, j))

#3개 벽세우는 조합 구하기
wall = list(combinations(empty, 3))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def spread(x, y):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            if new_graph[nx][ny] == 0:
                new_graph[nx][ny] = 2
                spread(nx, ny)

answer = -1
for w in wall:
    new_graph = copy.deepcopy(graph)
    for i in range(3):
        x, y = w[i]
        new_graph[x][y] = 1

    #바이러스 퍼트리기
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if new_graph[i][j] == 2 and not visited[i][j]:
                spread(i, j)

    #0인 곳 세기
    cnt = 0
    for i in range(n):
        for j in range(m):
            if new_graph[i][j] == 0:
                cnt += 1
    answer = max(cnt, answer)

print(answer)


