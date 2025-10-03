def solution(graph, skills):
    answer = 0
    
    n = len(graph)
    m = len(graph[0])
    #뭔가 누적합 느낌인디..............
    board = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for skill in skills:
        tp, r1, c1, r2, c2, degree = skill
        if tp == 1:
            board[r1][c1] -= degree
            board[r1][c2+1] += degree
            board[r2+1][c1] += degree
            board[r2+1][c2+1] -= degree
        else:
            board[r1][c1] += degree
            board[r1][c2+1] -= degree
            board[r2+1][c1] -= degree
            board[r2+1][c2+1] += degree

    # 행 누적합
    for i in range(n+1):
        for j in range(1, m+1):
            board[i][j] += board[i][j-1]

    # 열 누적합
    for j in range(m+1):
        for i in range(1, n+1):
            board[i][j] += board[i-1][j]
    
    for i in range(n):
        for j in range(m):
            graph[i][j] += board[i][j] 
            if graph[i][j] >= 1:
                answer += 1
            
    return answer