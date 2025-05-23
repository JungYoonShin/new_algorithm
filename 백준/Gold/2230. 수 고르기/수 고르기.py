import sys
input=sys.stdin.readline

n, m = map(int, input().split())
num = [int(input()) for _ in range(n)]
num.sort()

pointer_a = 0
pointer_b = 0

result = max(num) - min(num)
while pointer_a <= pointer_b and pointer_b < n:
    if num[pointer_b] - num[pointer_a] >= m:
        result = min(result, num[pointer_b] - num[pointer_a])
        pointer_a += 1
    else:
        pointer_b += 1


print(result)