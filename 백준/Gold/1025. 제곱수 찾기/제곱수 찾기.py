import sys
import math
input=sys.stdin.readline

n, m = map(int, input().split())
num = [list(input().strip()) for _ in range(n)]

answer = []
for i in range(n):
    for j in range(m):
        #행의 등차수열(반대방향도 가능)
        for x in range(-n, n):
            #열의 등차수열(반대방향도 가능)
            for z in range(-m, m):
                if x!= 0 or z != 0:
                    result = ''
                    move_x, move_y = i, j
                    while 0<=move_x<n and 0<=move_y<m:
                        result += num[move_x][move_y]
                        if int(math.sqrt(int(result))) ** 2 == int(result):
                            answer.append(int(result))

                        move_x += x
                        move_y += z

if len(answer) == 0:
    print(-1)
else:
    print(max(answer))