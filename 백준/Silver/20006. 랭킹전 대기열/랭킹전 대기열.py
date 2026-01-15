p, m = map(int, input().split())
player = [list(input().split()) for _ in range(p)]

player_dict = {}
for level, name in player:
    player_dict[name] = int(level)

rooms = []
for level, name in player:
    level = int(level)

    for room in rooms:
        if len(room[1]) < m and room[0] - 10 <= level <= room[0] + 10:
            room[1].append(name)
            break
    else:
        rooms.append([level, [name]])

for room in rooms:
    if len(room[1]) == m:
        print("Started!")
    else:
        print("Waiting!")

    for n in sorted(room[1]):
        print(player_dict[n], n)
