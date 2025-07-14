from sys import stdin


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if c[a] < c[b]:
        parent[b] = a
    else:
        parent[a] = b


N, M, k = map(int, stdin.readline().split())
parent = [x for x in range(N+1)]
c = [0] + list(map(int, stdin.readline().split()))
for _ in range(M):
    a, b = map(int, stdin.readline().split())
    union(a, b)

ans = 0
for i in range(1, N+1):
    if i == find(i):
        ans += c[i]

print(ans if k >= ans else 'Oh no')