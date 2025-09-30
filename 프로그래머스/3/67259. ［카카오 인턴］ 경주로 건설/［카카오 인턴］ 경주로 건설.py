from collections import deque
answer = 1e9

def solution(board):
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n = len(board)
    
    visited = [[False for i in range(n)] for _ in range(n)]
    graph = [[1e9 for _ in range(n)] for _ in range(n)]

    def bfs(d):
        q = deque([(0, 0, d, 0)])
        graph[0][0] = 0
        
        while q:
            a, b, direction, cost = q.popleft()
            
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                
                if 0<=nx<n and 0<=ny<n:
                    if board[nx][ny] == 0:
                        if direction == i:
                            new_cost = cost + 100
                        if direction != i:
                            new_cost = cost + 600
                        if new_cost <= graph[nx][ny]:
                            graph[nx][ny] = new_cost
                            q.append((nx, ny, i, new_cost))
        
        return graph[n-1][n-1]
    
    return min(bfs(3), bfs(1))
