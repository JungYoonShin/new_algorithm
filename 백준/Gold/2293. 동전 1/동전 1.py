import sys

input = sys.stdin.readline

n, k = map(int, input().split())
price = [int(input()) for _ in range(n)]
dp = [0] * 100001
dp[0] = 1

for coin in price:
    for j in range(coin, k+1):
        dp[j] += dp[j-coin]
print(dp[k])