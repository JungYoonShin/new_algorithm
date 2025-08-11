import sys
input = sys.stdin.readline
from bisect import bisect_left

n, m = map(int, input().split())

c = []
power = []

for _ in range(n):
    a, b = input().split()
    c.append(a)
    power.append(int(b))

for _ in range(m):
    p = int(input())
    idx = bisect_left(power, p)
    print(c[idx])
