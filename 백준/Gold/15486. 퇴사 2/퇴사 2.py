import sys
import math
input = sys.stdin.readline

n = int(input())
sangdam = []
dp = [0] * (n + 1)
for _ in range(n):
    sangdam.append(list(map(int, input().split())))

profit = 0
for i in range(n):
    profit = max(profit, dp[i])
    if i + sangdam[i][0] > n:
        continue
    dp[i+sangdam[i][0]] = max(profit+sangdam[i][1], dp[i+sangdam[i][0]])
print(max(dp))

