from collections import deque

n, m = map(int, input().split())
jump = {}

# 사다리 입력
for _ in range(n):
    a, b = map(int, input().split())
    jump[a] = b

# 뱀 입력
for _ in range(m):
    a, b = map(int, input().split())
    jump[a] = b

visited = [False] * 101
q = deque([(1, 0)])  # (현재 위치, 이동 횟수)

while q:
    now, cnt = q.popleft()

    if now == 100:
        print(cnt)
        break

    for dice in range(1, 7):
        next_pos = now + dice
        if next_pos > 100:
            continue

        if next_pos in jump:  # 사다리 또는 뱀
            next_pos = jump[next_pos]

        if not visited[next_pos]:
            visited[next_pos] = True
            q.append((next_pos, cnt + 1))
