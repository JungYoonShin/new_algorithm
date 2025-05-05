import sys
input=sys.stdin.readline

n = int(input())

start = 1
end = 1
result = 0
sum = 0

while start <= n:
    while end <= n and sum < n:
        sum += end
        end += 1

    if sum == n:
        result += 1

    sum -= start
    start += 1

print(result)