import sys
input=sys.stdin.readline

n = int(input())
m = int(input())

cost = [[1e9 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if cost[a-1][b-1] != 1e9:
        cost[a-1][b-1] = min(cost[a-1][b-1], c)
    else:
        cost[a - 1][b - 1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                cost[i][j] = 0
                continue
            if cost[i][k] + cost[k][j] < cost[i][j]:
                cost[i][j] = cost[i][k] + cost[k][j]

for i in range(n):
    for j in range(n):
        print(0 if cost[i][j] == 1e9 else cost[i][j], end=" ")
    print()