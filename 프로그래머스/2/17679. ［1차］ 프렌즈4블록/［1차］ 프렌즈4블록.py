def solution(m, n, board):
    answer = 0
    remove_set = set('*')
    board = list(map(list, board))
    while True:
        new_board = list(x[:] for x in board)
        total_set = set()
        
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == '':
                    continue
                #네개 값이 같음 터트려야 함 (터트릴 애들 *로 바꾸기)
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    new_board[i][j], new_board[i+1][j], new_board[i][j+1], new_board[i+1][j+1] = '*', '*','*','*'
                    total_set.update({(i, j), (i+1, j), (i, j+1), (i+1, j+1)})
                    
        if not total_set:
            break
        
        #터트릴 애들 확인끝났으면, 열마다 * 삭제하고 빈 부분은 빈 문자열 채우기
        new_board = list(map(list, zip(*new_board))) # 행 <-> 열 변환
        for i in range(n):
            len_i = len(new_board[i])
            new_board[i] = [x for x in new_board[i] if x not in remove_set]
            while len(new_board[i]) < len_i:
                new_board[i].insert(0, '')
        
        new_board = list(map(list, zip(*new_board))) # 다시 원상 복구
        board = list(x[:] for x in new_board)
        answer += len(total_set)
        

    return answer