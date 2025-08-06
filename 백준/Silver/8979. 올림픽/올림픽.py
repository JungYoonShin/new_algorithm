import sys
input = sys.stdin.readline
from collections import defaultdict

n, k = map(int, input().split())
country = []

for _ in range(n):
    num, gold, silver, bronze = map(int, input().split())
    country.append((num, gold, silver, bronze))

    if num == k:
        find = (gold, silver, bronze)

country.sort(key=lambda x: (-x[1], -x[2], -x[3]))

answer = 0

for i in range(1, n):
    if country[i][1:] == find:
        print(i+1)
        break