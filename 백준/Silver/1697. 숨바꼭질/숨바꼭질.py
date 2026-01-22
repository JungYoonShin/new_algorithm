n, k = map(int, input().split())

#수빈이의 위치가 더 클 수 있다.
if n == k:
    print(0)
elif n > k:
    print(n-k)
else:

    time = [1e9] * (k+2)
    time[n] = 0
    if n > 0:
        for i in range(0, n):
            time[i] = n - i

    for i in range(n+1, k+2):
        if i % 2 == 0:
            small = min(time[i-1], time[i//2])
            time[i] = small + 1

            time[i-1] = min(time[i]+1, time[i-1])
        else:
            time[i] = time[i-1] + 1

    print(time[k])



