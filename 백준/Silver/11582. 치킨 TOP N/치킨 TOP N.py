n = int(input())
num = list(map(int, input().split()))
k = int(input())

time = n // k

for i in range(time, n+1, time):
    num[i-time:i] = sorted(num[i-time:i])

print(*num)
