import sys

input = sys.stdin.readline

N = int(input())
A = [[*map(int, input().split())] for _ in range(N)]
for a, b in A:
  print(sum((a < c) * (b < d) for c, d in A) + 1)