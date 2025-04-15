from collections import deque
def solution(maps):
    answer = 0
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    def bfs(x, y):
        q = deque([(x, y)])
        
        visited[x][y] = True
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if not visited[nx][ny] and maps[nx][ny] != 0:
                        visited[nx][ny] = 1
                        maps[nx][ny] = maps[x][y] + 1
                        q.append((nx, ny))
        
    
    bfs(0, 0)
    if maps[n-1][m-1] == 1:
        return -1
    return maps[n-1][m-1]
    
    return answer