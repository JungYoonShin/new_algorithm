from collections import deque
def solution(places):
    answer = []
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    def bfs(i, j):
        q = deque([(i, j, 0)])
        visited = [[False for _ in range(5)] for _ in range(5)]
        
        while q:
            a, b, depth = q.popleft()
            visited[a][b] = True
            if place[a][b] == 'P' and 1<=depth<=2:
                return 0
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                
                if 0<=nx<5 and 0<=ny<5:
                    if not visited[nx][ny] and place[nx][ny] != 'X':
                        q.append((nx, ny, depth+1))
            
        return 1
    
    for place in places:
        flag = False
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if bfs(i, j) == 0:
                        flag = True
                        answer.append(0)
                        break
            if flag:
                break
        if not flag:
            answer.append(1)
        
    return answer