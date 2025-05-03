import sys
from heapq import heappush, heappop
input=sys.stdin.readline


n = int(input())
nums = []
for _ in range(n):
    num = int(input())
    if num != 0:
        heappush(nums, num)
    elif num == 0:
        if len(nums) == 0:
            print(0)
        else:
            print(heappop(nums))
