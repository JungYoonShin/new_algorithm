import sys

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice = [0, 0, 0, 0, 0, 0, 0]

def move(direction):
    a, b, c, d, e, f = dice[1], dice[2], dice[3], dice[4], dice[5], dice[6]
    #동쪽으로 이동
    if direction == 1:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = d, b, a, f, e, c

    #서쪽으로 이동
    elif direction == 2:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = c, b, f, a, e, d

    #남쪽으로 이동
    elif direction == 3:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = b, f, c, d, a, e

    #북쪽으로 이동
    else:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = e, a, c, d, f, b

n, m, x, y, k = map(int, input().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

d = list(map(int, input().split()))
for i in d:
    x += dx[i-1]
    y += dy[i-1]

    if x < 0 or x >= n or y < 0 or y >= m:
        x -= dx[i - 1]
        y -= dy[i - 1]
        continue

    move(i)
    if maps[x][y] == 0:
        maps[x][y] = dice[-1]
    else:
        dice[-1] = maps[x][y]
        maps[x][y] = 0
    print(dice[1])