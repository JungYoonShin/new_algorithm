import sys
from collections import deque

input = sys.stdin.readline

n, m, fuel = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

start_x, start_y = map(int, input().split())
start_x -= 1
start_y -= 1

customers = []
for _ in range(m):
    x, y, to_x, to_y = map(int, input().split())
    customers.append([x-1, y-1, to_x-1, to_y-1])

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def getDistance(a, b):
    distance_map = [[-1 for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque([(a, b, 0)])
    visited[a][b] = True
    distance_map[a][b] = 0

    while q:
        x, y, distance = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and maps[nx][ny] == 0:
                    visited[nx][ny] = True
                    distance_map[nx][ny] = distance + 1
                    q.append((nx, ny, distance + 1))
    return distance_map

def moveToDestination(d, customer_x, customer_y, to_go_x, to_go_y):
    global fuel, start_x, start_y

    fuel -= d
    if fuel < 0:
        return -1

    distance_map = getDistance(customer_x, customer_y)
    distance = distance_map[to_go_x][to_go_y]

    #도착지까지 갈 수가 없는 경우(경로가 없음)
    if distance == -1:
        return -1

    fuel -= distance
    if fuel < 0:
        return -1

    fuel += distance * 2
    start_x, start_y = to_go_x, to_go_y
    return True

for _ in range(m):
    distance_map = getDistance(start_x, start_y)

    customers.sort(key=lambda c: (distance_map[c[0]][c[1]], c[0], c[1]))

    x, y, to_x, to_y = customers.pop(0)

    if distance_map[x][y] == -1:
        fuel = -1
        break

    result = moveToDestination(distance_map[x][y], x, y, to_x, to_y)
    if result != True:
        fuel = -1
        break

print(fuel)
