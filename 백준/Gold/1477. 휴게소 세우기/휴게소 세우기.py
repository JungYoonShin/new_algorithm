import sys

input = sys.stdin.readline

n, m, l = map(int, input().split())
rest = list(map(int, input().split()))

rest.append(0)
rest.append(l)
rest.sort()

start, end = 1, l
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(1, len(rest)):
        if rest[i]-rest[i-1] > mid:
            #필요한 휴게소 수
            count += (rest[i]-rest[i-1]-1)//mid

    if count > m:
        start = mid+1
    else:
        result = mid
        end= mid-1

print(result)