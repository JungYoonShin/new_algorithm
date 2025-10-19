from collections import deque

#C를 연결하기 위해 설치해야 하는 거울 개수의 최솟값

w, h = map(int, input().split()) #w(가로), h(세로)
board = [list(input().rstrip()) for _ in range(h)]

#설치할 수 있는 거울('/', '\')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

mirror_location = []
for i in range(h):
    for j in range(w):
        if board[i][j] == 'C':
            mirror_location.append([i, j])


startx, starty = mirror_location[0]
endx, endy = mirror_location[1]

mirror = [[10**9 for _ in range(w)] for _ in range(h)]
mirror[startx][starty] = 0
def bfs(startx, starty):
    q = deque([(startx, starty)])
    visited = [[False for _ in range(w)] for _ in range(h)]

    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            while 0<=nx<h and 0<=ny<w and board[nx][ny] != '*':
                if mirror[nx][ny] < mirror[x][y] + 1:
                    break
                if mirror[nx][ny] == 10**9:
                    mirror[nx][ny] = mirror[x][y] + 1
                    q.append((nx, ny))
                nx += dx[i]
                ny += dy[i]

bfs(startx, starty)
print(mirror[endx][endy]-1)
# print(*mirror, sep="\n")




