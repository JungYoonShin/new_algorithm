# 백준 12100 (네 코드 스타일 최대한 유지해서 "고치기만" 한 버전)

import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]   # 0:위 1:아래 2:왼 3:오
dy = [0, 0, -1, 1]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def move_one(board, d):
    # d 방향으로 한 번 이동한 새 보드 반환
    new = [row[:] for row in board]
    merged = [[False]*n for _ in range(n)]

    if d == 0:  # 위
        rng_i = range(1, n)
        rng_j = range(n)
    elif d == 1:  # 아래
        rng_i = range(n-2, -1, -1)
        rng_j = range(n)
    elif d == 2:  # 왼
        rng_i = range(n)
        rng_j = range(1, n)
    else:  # 오른
        rng_i = range(n)
        rng_j = range(n-2, -1, -1)

    for i in rng_i:
        for j in rng_j:
            if new[i][j] == 0:
                continue

            x, y = i, j
            while True:
                nx, ny = x + dx[d], y + dy[d]
                if not (0 <= nx < n and 0 <= ny < n):
                    break

                if new[nx][ny] == 0:
                    new[nx][ny] = new[x][y]
                    new[x][y] = 0
                    x, y = nx, ny
                else:
                    if new[nx][ny] == new[x][y] and not merged[nx][ny]:
                        new[nx][ny] *= 2
                        new[x][y] = 0
                        merged[nx][ny] = True
                    break

    return new

def move(tries):
    global graph, ans

    ans = max(ans, max(map(max, graph)))
    if tries == 5:
        return

    original = [row[:] for row in graph]
    for d in range(4):
        graph = move_one(original, d)
        move(tries + 1)
    graph = original

move(0)
print(ans)
