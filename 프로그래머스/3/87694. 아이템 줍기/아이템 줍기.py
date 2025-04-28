from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    graph = [[-1 for _ in range(210)] for _ in range(210)]
    visited = [[0 for _ in range(210)] for _ in range(210)]
    
    cx, cy, ix, iy = characterX*2, characterY*2, itemX*2, itemY*2
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    def bfs(x, y):
        q = deque([(x, y)])
        visited[x][y] = 1
        
        while q:
            x, y = q.popleft()
            
            if x == ix and y == iy:
                return visited[x][y] //2
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < 210 and 0 <= ny < 210:
                    if not visited[nx][ny] and graph[nx][ny] == 1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
                    
    
    for r in rectangle:
        left_x, left_y, right_x, right_y = map(lambda x : x*2, r)
        for i in range(left_x, right_x+1):
            for j in range(left_y, right_y+1):
                #내부에 있는 건 0으로 
                if left_x < i < right_x and left_y < j < right_y:
                    graph[i][j] = 0
                    
                elif graph[i][j] != 0:
                    graph[i][j] = 1
                    
    
    return bfs(cx, cy)
        
        
