import sys
input=sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
sum = [0] * (n+1)
sum[0], sum[1] = 0, nums[0]

for i in range(1, n+1):
    sum[i] = sum[i-1] + nums[i-1]

start = 1
end = 1
result = 0
while end <= n:
    part_sum = sum[end] - sum[start - 1]

    if part_sum < m:
        end += 1
    elif part_sum > m:
        start += 1
    else:
        result += 1
        end += 1

print(result)