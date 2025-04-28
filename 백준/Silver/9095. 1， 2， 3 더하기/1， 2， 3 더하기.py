import sys

input = sys.stdin.readline

T = int(input())
cnt = [0] * 12
cnt[1], cnt[2], cnt[3] = 1, 2, 4

def sum(x):
    for i in range(4, x+1):
        cnt[i] = cnt[i-1] + cnt[i-2] + cnt[i-3]
    return cnt[i]


for _ in range(T):
    n = int(input())

    if n > 3:
        print(sum(n))
    else:
        print(cnt[n])
