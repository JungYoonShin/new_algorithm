import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [1e9 for _ in range(k+1)]
dp[0] = 0

for c in coin:
    for i in range(c, k+1):
        dp[i] = min(dp[i], dp[i-c] + 1)

if dp[k] != 1e9:
    print(dp[k])
else:
    print(-1)