from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    board = [[-1 for _ in range(210)] for _ in range(210)]
    
    characterX, characterY, itemX, itemY = characterX*2, characterY*2, itemX*2, itemY*2
    
    #사각형 내부에 있는 점들은 이동 못하게 처리
    for rec in rectangle:
        lx, ly, rx, ry = map(lambda x : x*2, rec)
        
        for i in range(lx, rx+1):
            for j in range(ly, ry+1):
                if lx < i < rx and ly < j < ry:
                    board[i][j] = 1
                elif board[i][j] != 1:
                    board[i][j] = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cost = [[0 for _ in range(210)] for _ in range(210)]
    
    def bfs():
        q = deque([(characterX, characterY)])
        visited = [[False for _ in range(210)] for _ in range(210)]
        visited[characterX][characterY] = True
        
        while q:
            x, y = q.popleft()
            
            if x == itemX and y == itemY:
                break
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<210 and 0<=ny<210:
                    if not visited[nx][ny] and board[nx][ny] == 0:
                        q.append((nx, ny))
                        cost[nx][ny] = cost[x][y] + 1
                        visited[nx][ny] = True
                        
        return cost[itemX][itemY]//2
    
    return bfs()