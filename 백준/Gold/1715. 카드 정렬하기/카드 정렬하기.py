import sys
from heapq import heappush, heappop, heapify

input=sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
heapify(nums)
result = []

while len(nums)>=2:
    a = heappop(nums)
    b = heappop(nums)
    result.append(a+b)
    heappush(nums, a+b)

print(sum(result))