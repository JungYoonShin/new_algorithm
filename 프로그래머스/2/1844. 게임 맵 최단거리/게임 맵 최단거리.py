from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(maps):
    q = deque([(0, 0, 1)])
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    
    while q:
        x, y, dist = q.popleft()
        if x == n-1 and y == m-1:
            return dist
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    q.append((nx, ny, dist+1))
                    visited[nx][ny] = 1
    return False
            

def solution(maps):
    answer = bfs(maps)
    
    if answer:
        return answer
    return -1
    