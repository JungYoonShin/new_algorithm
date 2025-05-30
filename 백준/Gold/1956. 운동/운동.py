import sys
input = sys.stdin.readline

v, e = map(int, input().split())

graph = [[1e9 for _ in range(v+1)] for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a][b] = c

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

result = 1e9
for i in range(1, v+1):
    result = min(result, graph[i][i])

if result == 1e9:
    print(-1)
else:
    print(result)
