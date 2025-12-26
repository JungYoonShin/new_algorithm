from collections import deque
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs():
        q = deque([(0, 0)])
        global visited
        visited = [[False for _ in range(m)] for _ in range(n)]
        visited[0][0] = 1
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                    if maps[nx][ny] == 1:
                        q.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1
                    
    
    bfs()
    answer = visited[n-1][m-1]
    if answer == 0:
        return -1
        
    return answer