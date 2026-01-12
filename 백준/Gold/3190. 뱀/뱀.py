import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
k = int(input())

maps = [[0] * (n+1) for _ in range(n+1)]

direction = {}
for _ in range(k):
    x, y = map(int, input().split())
    maps[x-1][y-1] = 2

L = int(input())
for _ in range(L):
    x, c = input().split()
    direction[int(x)] = c

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d = 0
x, y = 0, 0
cnt = 0
snakes = deque([(0, 0)])

def turn(cnt):
    global d
    if direction[cnt] == 'L':
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4

while True:
    cnt += 1
    x += dx[d]
    y += dy[d]

    if x < 0 or x >= n or y < 0 or y >= n:
        break
    if maps[x][y] == 2:
        maps[x][y] = 1
        snakes.append((x, y))
        if cnt in direction:
            turn(cnt)
    elif maps[x][y] == 0:
        maps[x][y] = 1
        snakes.append((x, y))
        a, b = snakes.popleft()
        maps[a][b] = 0
        if cnt in direction:
            turn(cnt)
    else:
        break
print(cnt)