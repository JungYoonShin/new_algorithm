def solution(board):
    answer = -1
    n = 3
    
    first, second = 0, 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'O':
                first += 1
            if board[i][j] == 'X':
                second += 1
    
    if first < second or first - second > 1:
        return 0
    
    #빙고 개수 찾기
    #행별 빙고
    row_bingo, col_bingo, cross_bingo = [0, 0], [0, 0], [0, 0]
    for i in range(n):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'O':
                row_bingo[0] += 1
            if board[i][0] == 'X':
                row_bingo[1] += 1
    #열별 빙고
    for i in range(n):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'O':
                col_bingo[0] += 1
            if board[0][i] == 'X':
                col_bingo[1] += 1
    
    #대각선 빙고
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'O':
            cross_bingo[0] += 1
        if board[0][0] == 'X':
            cross_bingo[1] += 1
            
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'O':
            cross_bingo[0] += 1
        if board[0][2] == 'X':
            cross_bingo[1] += 1
    
    total_O = cross_bingo[0] + row_bingo[0] + col_bingo[0]
    total_x = cross_bingo[1] + row_bingo[1] + col_bingo[1]
    
    if total_O >= 1 and total_x >= 1:
        return 0
    
    if total_O >= 1 and first != second + 1:
        return 0
    
    if total_x >= 1 and first != second:
        return 0
    

    return 1