import sys

input = sys.stdin.readline

#한수가 집까지도 도착하는 경우 중 거리가 K인 가짓수를 구하기
r, c, k = map(int, input().split()) #행, 열

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

board = [list(input().rstrip()) for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]
answer = 0

def dfs(x, y, depth):
    global answer

    if x == 0 and y == c-1:
        if depth == k:
            answer += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<r and 0<=ny<c:
            if not visited[nx][ny] and board[nx][ny] == '.':
                visited[nx][ny] = True
                dfs(nx, ny, depth+1)
                visited[nx][ny] = False
    return

visited[r-1][0] = True
dfs(r-1, 0, 1)
print(answer)