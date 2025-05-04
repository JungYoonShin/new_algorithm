import sys
input=sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
sum = [0] * (n+1)
sum[0], sum[1] = 0, nums[0]

for i in range(2, n+1):
    sum[i] = sum[i-1] + nums[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    print(sum[j] - sum[i-1])
