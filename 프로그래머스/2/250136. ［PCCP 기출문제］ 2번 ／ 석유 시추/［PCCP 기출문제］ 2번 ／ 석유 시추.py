from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[0]*m for _ in range(n)]
    island_size = dict()
    color = 1
    
    def bfs(x, y, color):
        q = deque()
        q.append((x, y))
        visited[x][y] = color
        
        cnt = 1
        
        while q:
            cx, cy = q.popleft()
            
            for d in range(4):
                nx = cx + dx[d]
                ny = cy + dy[d]
                
                if 0 <= nx < n and 0 <= ny < m:
                    if land[nx][ny] == 1 and visited[nx][ny] == 0:
                        visited[nx][ny] = color
                        q.append((nx, ny))
                        cnt += 1
                        
        return cnt
    
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                size = bfs(i, j, color)
                island_size[color] = size
                color += 1
    
    answer = 0
    
    for col in range(m):
        seen = set()
        total = 0
        
        for row in range(n):
            if land[row][col] == 1:
                seen.add(visited[row][col])
        
        for c in seen:
            total += island_size[c]
        
        answer = max(answer, total)
    
    return answer
