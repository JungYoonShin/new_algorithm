from collections import deque
def solution(board):
    answer = 1e9
    #경주로를 건설하는 데 필요한 최소 비용
    #0빈칸 1벽 / 직선 -> 100원, 코너 -> 500원
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n = len(board)
    
    def bfs(d):
        q = deque([(0, 0, 0, d)])
        total = [[1e9 for _ in range(n)] for _ in range(n)]
        total[0][0] = 0
        
        while q:
            x, y, cost, direction = q.popleft()
            
#             if x == n-1 and y == n-1:
#                 answer = min(answer, cost)
#                 return

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<n and 0<=ny<n:
                    if board[nx][ny] == 0:
                        if i == direction:
                            new_cost = cost+ 100
                        else:
                            new_cost = cost + 600
                        
                        if new_cost < total[nx][ny]:
                            total[nx][ny] = new_cost
                            q.append((nx, ny, new_cost, i))
        return total[-1][-1]
    
    answer = min(bfs(1), bfs(3))
    return answer