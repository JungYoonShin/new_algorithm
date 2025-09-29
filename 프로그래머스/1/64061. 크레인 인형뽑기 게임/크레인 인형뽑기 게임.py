def solution(board, moves):
    answer = 0
    
    bowl = []
    
    board = list(map(list, zip(*board[::-1])))
    n = len(board)
    for i in range(n):
        while board[i] and board[i][-1] == 0:
            board[i].pop()

            
    for move in moves:
        if not board[move-1]:
            continue
        
        bowl.append(board[move-1].pop())
        
        if len(bowl) == 1:
            continue
        
        if bowl[-1] == bowl[-2]:
            bowl.pop()
            bowl.pop()
            answer += 2
            
    return answer