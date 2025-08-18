import sys

input = sys.stdin.readline

left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
         (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, rate) for x, y, rate in left]
up = [(y, x, rate) for x, y, rate in left]
down = [(-y, x, rate) for x, y, rate in left]

d = [left, down, right, up]
result = 0

def move(cnt, dx, dy, direction):
    global result, now_x, now_y
    for _ in range(cnt+1):
        now_x, now_y = now_x + dx, now_y + dy
        if now_x < 0 or now_y < 0:
            break

        sum = 0 #퍼진 모래 양
        for x, y, rate in d[direction]:
            nx, ny = now_x + x, now_y + y
            if rate == 0: #a위치(퍼지고 남은 모래양)
                sand = maps[now_x][now_y] - sum
            else: #퍼지는 모래들
                sand = int(maps[now_x][now_y] * rate)
                sum += sand

            if 0<= nx < n and 0 <= ny < n:
                maps[nx][ny] += sand
            else:
                result += sand


n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
now_x, now_y = n//2, n//2
for i in range(n):
    if i % 2 == 0:
        move(i, 0, -1, 0)
        move(i, 1, 0,  1)
    else:
        move(i, 0, 1, 2)
        move(i, -1, 0, 3)

print(result)