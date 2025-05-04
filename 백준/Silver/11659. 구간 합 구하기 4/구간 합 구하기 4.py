import sys
input=sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
sum = [0] * n
sum[0] = nums[0]

for i in range(1, n):
    sum[i] = sum[i-1] + nums[i]

for _ in range(m):
    i, j = map(int, input().split())
    if i == 1:
        if j==1:
            print(sum[0])
        else:
            print(sum[j - 1])
    else:
        print(sum[j-1] - sum[i-2])
