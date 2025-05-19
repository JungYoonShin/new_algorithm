import sys
input=sys.stdin.readline

n, m = map(int, input().split())

parent = [x for x in range(n)]
graph = [[] for _ in range(n)]

def getParent(x):
    if parent[x] != x:
        parent[x] = getParent(parent[x])
    return parent[x]

def union(x, y):
    a = getParent(x)
    b = getParent(y)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

result = 0
for i in range(m):
    a, b = map(int, input().split())
    if getParent(a) == getParent(b):
        result = i+1
        break
    union(a, b)
print(result)