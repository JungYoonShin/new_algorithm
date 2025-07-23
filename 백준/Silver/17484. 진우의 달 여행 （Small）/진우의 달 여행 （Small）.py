import sys

input = sys.stdin.readline

# 움직일 수 있는 방향
d = [(1, -1), (1, 0), (1, 1)]

#우주선은 전에 움직인 방향으로 움직일 수 없다. 즉, 같은 방향으로 두번 연속으로 움직일 수 없다.
#목표: 연료를 최대한 아끼며 지구의 어느위치에서든 출발하여 달의 어느위치든 착륙하는 것

n, m = map(int, input().split())
fuel = [list(map(int, input().split())) for _ in range(n)]

answer = [[[1e9] * 3 for _ in range(m)] for _ in range(n)]

for i in range(m):
    for j in range(3):
        answer[0][i][j] = fuel[0][i]

for i in range(1, n):
    for j in range(m):
        for dir in range(3):
            if 0 <= j+d[dir][1] < m:
                if dir == 0:
                    answer[i][j][dir] = min(answer[i-1][j-1][1], answer[i-1][j-1][2]) + fuel[i][j]
                elif dir == 1:
                    answer[i][j][dir] = min(answer[i - 1][j][0], answer[i - 1][j][2]) + fuel[i][j]
                else:
                    answer[i][j][dir] = min(answer[i - 1][j+1][0], answer[i - 1][j+1][1]) + fuel[i][j]

a = 1e9
for i in range(m):
    a = min(a, min(answer[-1][i]))
print(a)