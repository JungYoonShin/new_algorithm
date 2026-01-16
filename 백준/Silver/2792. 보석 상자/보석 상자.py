n, m = map(int, input().split())
jealous = [int(input()) for _ in range(m)]

start = 1
end = max(jealous)

while start<=end:
    mid = (start+end) // 2
    sum = 0
    for j in jealous:
        sum += (j+mid-1) // mid

    if sum > n:
        start = mid + 1
    else:
        end = mid - 1
        result = mid

print(result)