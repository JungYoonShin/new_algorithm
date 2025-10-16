import sys

input = sys.stdin.readline

#볼을 같은 색끼리 모을 수 있는 최소 이동 횟수
#R 또는 B 중 한 종류만 주어질 수도 있으며, 이 경우 답은 0이 된다.
#색깔은 처음에 빨간색 or 파란색

n = int(input())
ball = list(input().rstrip())
b, r = 0, 0
for i in range(n):
    if ball[i] == 'B':
        b += 1
    else:
        r += 1

if b == 0 or r == 0:
    print(0)
    exit()

#빨간색(오른쪽, 왼쪽)
cntr1, cntr2, cntb1, cntb2 = 0, 0, 0, 0
flag = False
for i in range(n-1, -1, -1):
    if ball[i] == 'B':
        flag = True

    if ball[i] == 'R' and flag == True:
        cntr1 += 1
#빨간색(오른쪽, 왼쪽)
flag = False
for i in range(n):
    if ball[i] == 'B':
        flag = True

    if ball[i] == 'R' and flag == True:
        cntr2 += 1

#파란색(오른, 왼쪽)
flag = False
for i in range(n - 1, -1, -1):
    if ball[i] == 'R':
        flag = True

    if ball[i] == 'B' and flag == True:
        cntb1 += 1

flag = False
for i in range(n):
    if ball[i] == 'R':
        flag = True

    if ball[i] == 'B' and flag == True:
        cntb2 += 1

print(min(min(cntr1, cntr2), min(cntb1, cntb2)))
