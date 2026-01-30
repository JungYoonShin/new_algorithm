from collections import deque
def solution(places):
    answer = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x, y, place):
        q = deque([(x, y, 0)])
        visited = [[False for _ in range(5)] for _ in range(5)]
        visited[x][y] = True
        while q:
            a, b, dist = q.popleft()
            if 0<dist<=2 and place[a][b] == 'P':
                return False
            for d in range(4):
                nx, ny = a + dx[d], b + dy[d]
                if 0<=nx<5 and 0<=ny<5:
                    if not visited[nx][ny] and place[nx][ny] != 'X':
                        q.append((nx, ny, dist+1))
                        visited[nx][ny] = True
        return True
    
    for place in places:
        flag = False
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if not bfs(i, j, place):
                        answer.append(0)
                        flag = True
                        break
            if flag:
                break
        if not flag:
            answer.append(1)
    return answer