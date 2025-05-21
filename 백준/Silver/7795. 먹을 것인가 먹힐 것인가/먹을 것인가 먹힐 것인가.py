import sys
input=sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    cnt = 0
    pointer_b = 0
    for pointer_a in range(n):
        while pointer_b < m and b[pointer_b] < a[pointer_a]:
            pointer_b += 1
        cnt += pointer_b
    print(cnt)