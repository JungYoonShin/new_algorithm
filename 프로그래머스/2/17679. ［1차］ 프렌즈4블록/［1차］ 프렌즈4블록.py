def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]

    def delete(board, r, c):
        col = []
        
        for i in range(c):
            col_list = [board[j][i] for j in range(r) if board[j][i] != '-']
            
            for j in range(r-1, -1, -1):
                if col_list:
                    board[j][i] = col_list.pop()
                else:
                    board[j][i] = '*'
        return board
        
    while True:
        should_delete = set()

        # 2x2 같은 블록 찾기
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] not in ['-', '*'] and \
                   board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    should_delete.update({(i, j), (i+1, j), (i, j+1), (i+1, j+1)})

        if not should_delete:
            break

        for (x, y) in should_delete:
            board[x][y] = '-'
        answer += len(should_delete)

        # 블록 내리기
        board = delete(board, m, n)

    return answer
