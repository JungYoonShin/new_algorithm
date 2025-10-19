import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 외부공기 표시
def dfs(x, y, visited):
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny]:
                if board[nx][ny] == 0:
                    board[nx][ny] = 2  # 외부공기 표시
                    dfs(nx, ny, visited)
                elif board[nx][ny] == 2:
                    dfs(nx, ny, visited)

def melt():
    global board
    new_board = [row[:] for row in board]
    melted = False
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                cnt = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 2:
                        cnt += 1
                if cnt >= 2:
                    new_board[i][j] = 0
                    melted = True
    board = new_board
    return melted

time = 0
while True:
    # 외부공기 새로 갱신
    visited = [[False]*m for _ in range(n)]
    dfs(0, 0, visited)

    # 치즈 녹이기
    if not melt():
        break
    time += 1

print(time)