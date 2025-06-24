import sys
from collections import defaultdict
input = sys.stdin.readline

p, m = map(int, input().split())
player = [list(input().split()) for _ in range(p)]
rooms = []

for l, n in player:
    l = int(l)
    for room in rooms:
        level = room[0][0]
        if len(room) < m and level-10 <= l <= level+10:
            room.append((l, n))
            break
    else:
        rooms.append([(l, n)])
for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    room.sort(key=lambda x: x[1])
    for l, n in room:
        print(l, n)