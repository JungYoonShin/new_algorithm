import sys
input = sys.stdin.readline

n, k = map(int, input().split())
weight = [0]
value = [0]
for _ in range(n):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

result = -1e9

#배낭에 넣을 수 있는 물건들의 가치합의 최댓값
for i in range(1, n+1):
    for j in range(k+1):
        if j < weight[i]:
            dp[i][j] = dp[i-1][j]

        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])

        result = max(result, dp[i][j])


print(result)

