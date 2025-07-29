import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
move = [list(map(int, input().split())) for _ in range(n+m)]

result = 0
visited=[0]*101

def bfs(start, cnt):
    q = deque([(start, cnt)])
    visited[start] = 1

    while q:
        current, turn = q.popleft()

        for dice in range(1, 7):
            next_pos = current + dice
            if next_pos > 100:
                continue

            for a, b in move:
                if next_pos == a:
                    next_pos = b

            if not visited[next_pos]:
                if next_pos == 100:
                    print(turn+ 1)
                    exit()

                visited[next_pos] = True
                q.append((next_pos, turn + 1))


bfs(1, 0)