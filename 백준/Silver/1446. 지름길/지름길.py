import sys
input = sys.stdin.readline

n, d = map(int, input().split())
fast = [list(map(int, input().split())) for _ in range(n)]
fast.sort(key=lambda x: x[0])
dp = [x for x in range(10006)]

for i in range(0, d + 1):
    if i > 0:
        dp[i] = min(dp[i], dp[i - 1] + 1)
    for s, e, dist in fast:
        if e == i and e <= d:
            dp[e] = min(dp[e], dp[s] + dist)

print(dp[d])
