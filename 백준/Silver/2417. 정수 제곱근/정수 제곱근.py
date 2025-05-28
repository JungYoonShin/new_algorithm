import sys
input=sys.stdin.readline

n = int(input())

start = 0
end = 2 ** 63

result = 0
while start <= end:
    mid = (start + end) // 2

    if mid ** 2 >= n:
        result = mid
        end = mid-1
    else:
        start = mid+1
print(result)
