import sys
input=sys.stdin.readline

n = int(input())
height = [0 for _ in range(1001)]
for _ in range(n):
    L, H = map(int, input().split())
    height[L] = H

max_index = height.index(max(height))

max_height = 0
result = 0
for i in range(max_index+1):
    max_height = max(max_height, height[i])
    result += max_height

max_height = 0
for i in range(1000, max_index, -1):
    max_height = max(max_height, height[i])
    result += max_height

print(result)