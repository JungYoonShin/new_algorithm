import sys

input = sys.stdin.readline

n = int(input())
building = list(map(int, input().split()))

answer = [0] * n
for i in range(n):
    left_sum = 0
    right_sum = 0
    max_ = -1e9
    #오른쪽으로 나보다 큰값
    for right in range(i+1, n):
        s = (building[right] - building[i]) / (right-i)
        if s <= max_:
            continue
        max_ = max(max_, s)
        answer[i] += 1
        answer[right] += 1

print(max(answer))
