import sys

input = sys.stdin.readline
n, m, r = map(int, input().split())
board = [list(input().split()) for _ in range(n)]
r_list = list(map(int, input().split()))

for order in r_list:
    #1번 연산
    new_board = [row[:] for row in board]
    if order == 1:
        for i in range(n):
            new_board[(n-1)-i] = board[i]

    #2번 연산
    if order == 2:
        for i in range(n):
            for j in range(m):
                new_board[i][(m-1)-j] = board[i][j]

    #3번 연산
    if order == 3:
        new_board = [list(row) for row in zip(*board[::-1])]
        n, m = m, n

    #4번 연산
    if order == 4:
        new_board = [list(row) for row in zip(*new_board)]
        new_board.reverse()
        n, m = m, n

    #5번 연산
    if order == 5:
        for i in range(n):
            for j in range(m):
                #1번 그룹
                if 0<=i<n//2 and 0<=j<m//2:
                    new_board[i][j+(m//2)] = board[i][j]
                #2번 그룹
                elif 0<=i<n//2 and m//2<=j<m:
                    new_board[i+(n//2)][j] = board[i][j]

                #3번 그룹
                elif n//2<=i<n and m//2<=j<m:
                    new_board[i][j-(m//2)] = board[i][j]

                else:
                    new_board[i-(n//2)][j] = board[i][j]

    if order == 6:
        for i in range(n):
            for j in range(m):
                #1번 그룹
                if 0<=i<n//2 and 0<=j<m//2:
                    new_board[i+(n//2)][j] = board[i][j]
                #2번 그룹
                elif 0<=i<n//2 and m//2<=j<m:
                    new_board[i][j-(m//2)] = board[i][j]

                #3번 그룹
                elif n//2<=i<n and m//2<=j<m:
                    new_board[i-(n//2)][j] = board[i][j]

                else:
                    new_board[i][j+(m//2)] = board[i][j]

    board = new_board

for i in range(n):
    print(' '.join(board[i]))
