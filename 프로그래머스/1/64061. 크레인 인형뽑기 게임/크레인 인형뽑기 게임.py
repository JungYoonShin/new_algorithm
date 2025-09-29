def solution(board, moves):
    answer = 0
    
    bowl = []
    
    board = list(map(list, zip(*board[::-1])))
    n = len(board)
    for i in range(n):
        while board[i] and board[i][-1] == 0:
            board[i].pop()

    for move in moves:
        col = board[move - 1]
        if not col:
            continue

        doll = col.pop()
        if bowl and bowl[-1] == doll:
            bowl.pop()
            answer += 2
        else:
            bowl.append(doll)
            
    return answer