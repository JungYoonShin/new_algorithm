import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

v = [list(map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n+1)]
togo = list(map(int, input().split()))
for i in range(n):
    for j in range(n):
        if v[i][j] == 1:
            graph[i+1].append(j+1)

visited = [0] * (n+1)

def dfs(now):
    for v in graph[now]:
        if not visited[v]:
            visited[v] = 1
            dfs(v)

visited[togo[0]] = 1
dfs(togo[0])

for v in togo:
    if visited[v] == 0:
        print("NO")
        break
else:
    print("YES")
