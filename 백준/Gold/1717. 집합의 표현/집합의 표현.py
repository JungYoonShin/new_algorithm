import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n, m = map(int, input().split())

parent = [x for x in range(n+1)]

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

for _ in range(m):
    type, a, b, = map(int, input().split())
    #합치기(union)
    if type == 0:
        union(a, b)
    else:
        if getParent(a) == getParent(b):
            print("YES")
        else:
            print("NO")

