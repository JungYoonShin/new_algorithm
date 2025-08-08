import sys, copy
input = sys.stdin.readline


n = int(input())
dp = [1e9] * (n+1)
dp[0] = 0
dp[1] = 0

answer = [[] for _ in range(n+1)]
answer[1] = [1]

for i in range(2, n+1):
    if dp[i] > dp[i-1] + 1:
        dp[i] = dp[i-1] + 1
        answer[i] = [i-1]
    if i % 2 == 0 and dp[i//2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1
            answer[i] = [i//2]
    if i % 3 == 0 and dp[i//3] + 1 < dp[i]:
            dp[i] = dp[i//3] + 1
            answer[i] = [i//3]

path = [n]
while path[-1] != 1:
    path.append(answer[path[-1]][0])

print(dp[n])
print(*path)