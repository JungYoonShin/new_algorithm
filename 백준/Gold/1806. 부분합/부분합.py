import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

sumA = 0
end = 0
answer = 1e9
for start in range(n):
    while sumA < s and end < n:
        sumA += nums[end]
        end += 1

    if sumA >= s:
        answer = min(answer, end-start)

    sumA -= nums[start]

if answer == 1e9:
    print(0)
else:
    print(answer)
