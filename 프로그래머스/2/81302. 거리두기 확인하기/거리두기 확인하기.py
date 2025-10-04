def solution(places):
    answer = [1] * 5
    n = 5
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def dfs(idx, x, y, depth, visited):
        if depth >= 1:
            if board[x][y] == 'P':
                answer[idx] = 0
                return True
        if depth >= 2:
            return
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny] and board[nx][ny] != 'X':
                    visited[nx][ny] = True
                    if dfs(idx, nx, ny, depth+1, visited):
                        return True
                    visited[nx][ny] = False
                    
    
    for idx, place in enumerate(places):
        board = list(map(list, place))
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'P':
                    visited = [[False for _ in range(n)] for _ in range(n)]
                    visited[i][j] = True
                    dfs(idx, i, j, 0, visited)
        # print(answer)
        # print()
    
    return answer