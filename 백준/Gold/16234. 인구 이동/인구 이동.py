import sys

input = sys.stdin.readline
sys.setrecursionlimit(50000000)
n, l, r = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
island = []
def find_union(i, j):
    visited[i][j] = 1   
    global island
    island.append([i, j])

    for x in range(4):
        nx = i + dx[x]
        ny = j + dy[x]
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny] and l <= abs(people[nx][ny] - people[i][j]) <= r:
                find_union(nx, ny)

    return island

answer = 0
while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    union = []
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                island = []
                union_group = find_union(i, j)
                if len(union_group) >= 2:
                    union.append(union_group)
                    flag = True

    if not flag:
        print(answer)
        break

    for u in union:
        sum_people = 0
        for x, y in u:
            sum_people += people[x][y]
        for x, y in u:
            people[x][y] = sum_people // len(u)

    answer += 1