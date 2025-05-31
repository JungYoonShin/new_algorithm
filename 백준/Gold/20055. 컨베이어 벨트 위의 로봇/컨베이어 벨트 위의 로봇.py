import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
belt_age = deque(list(map(int, input().split())))
robot = deque([False] * (n))
result = 0

while True:
    result += 1

    #벨트와 로봇 함께 오른쪽으로 한 칸 이동
    belt_age.rotate(1)
    robot.rotate(1)

    #언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
    if robot[n-1] == True:
        robot[n-1] = False

    #가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동
    for i in range(n-2, -1, -1):
        #현재 칸에 로봇이 있고, 이동하려는 칸에 로봇이 없어야 함
        if robot[i] and not robot[i+1]:
            if belt_age[i+1] > 0:
                robot[i+1] = True
                robot[i] = False
                belt_age[i+1] -= 1

    #올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if belt_age[0] > 0:
        belt_age[0] -= 1
        robot[0] = True

    if robot[n-1] == True:
        robot[n-1] = False

    #내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다.
    if belt_age.count(0) >= k:
        break
        
        
print(result)

