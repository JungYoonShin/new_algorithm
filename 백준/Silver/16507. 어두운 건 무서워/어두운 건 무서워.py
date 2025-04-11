import sys

input = sys.stdin.readline

r, c, q = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(r)]

#누적합 구하기
prefix_sum = [[0]*(c+1) for _ in range(r+1)]

for i in range(1, r+1):
    for j in range(1, c+1):
        prefix_sum[i][j] = prefix_sum[i][j-1] + prefix_sum[i-1][j] - prefix_sum[i-1][j-1] + picture[i-1][j-1]

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    #부분합 구하기
    total = prefix_sum[r2][c2] - prefix_sum[r2][c1 - 1] - prefix_sum[r1 - 1][c2] + prefix_sum[r1 - 1][c1 - 1]
    count = (r2 - r1 + 1) * (c2 - c1 + 1)
    print(total // count)


