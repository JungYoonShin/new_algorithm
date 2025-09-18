def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]

    while True:
        should_delete = set()

        # 2x2 같은 블록 찾기
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != '-' and \
                   board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    should_delete.update({(i, j), (i+1, j), (i, j+1), (i+1, j+1)})

        if not should_delete:  # 더 이상 지울 게 없으면 종료
            break

        # 지우기
        for (x, y) in should_delete:
            board[x][y] = '-'
        answer += len(should_delete)

        # 블록 내리기
        for j in range(n):
            empty = ['-'] * m
            idx = m-1
            for i in range(m-1, -1, -1):
                if board[i][j] != '-':
                    empty[idx] = board[i][j]
                    idx -= 1
            for i in range(m):
                board[i][j] = empty[i]

    return answer
