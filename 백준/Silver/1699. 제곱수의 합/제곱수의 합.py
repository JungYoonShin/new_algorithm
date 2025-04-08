import sys
import math
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

for i in range(1, n+1):
    #제곱근 구하기
    dp[i] = i
    k = int(math.sqrt(i))+1
    for j in range(1, k):
        dp[i] = min(dp[i - j*j]+1, dp[i])

print(dp[n])

