import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())  # 코인개수
    coin = list(map(int, input().split()))
    m = int(input())  # 만들어야 할 금액
    dp = [0 for _ in range(m+1)]
    dp[0] = 1

    for c in coin:
        for i in range(c, m+1):
            dp[i] += dp[i-c]

    print(dp[m])

