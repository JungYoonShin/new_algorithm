from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(input().rstrip())
hamburger = []
human = []
for i in range(n):
    if s[i] == 'H':
        hamburger.append(i)
    else:
        human.append(i)

result = 0
while human and hamburger:
    if abs(human[0] - hamburger[0]) <= k:
        result += 1
        human.pop(0)
        hamburger.pop(0)
    elif human[0] < hamburger[0]:
        human.pop(0)
    else:
        hamburger.pop(0)

print(result)