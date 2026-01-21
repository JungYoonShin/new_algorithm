import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

sum_graph = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        sum_graph[i][j] = sum_graph[i][j-1] + sum_graph[i-1][j] - sum_graph[i-1][j-1] + graph[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(sum_graph[x2][y2] - sum_graph[x2][y1-1] - sum_graph[x1-1][y2] + sum_graph[x1-1][y1-1])

