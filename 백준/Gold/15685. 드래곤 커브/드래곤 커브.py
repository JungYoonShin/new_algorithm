n = int(input())

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

board = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(n):
    x, y, d, g = map(int, input().split())
    x, y = y, x

    directions = [d]
    board[x][y] = 1
    x, y = x + dx[d], y + dy[d]
    board[x][y] = 1


    for _ in range(g):
        for dir in directions[::-1]:
            new_dir = (dir+1) % 4
            x, y = x + dx[new_dir], y + dy[new_dir]
            board[x][y] = 1
            directions.append(new_dir)

result = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i][j+1] and board[i+1][j] and board[i+1][j+1]:
            result += 1
print(result)


