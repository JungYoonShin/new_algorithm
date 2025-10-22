def solution(places):
    answer = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    #응시자들끼리는 맨해튼 거리가 2이하면 안된다.
    def dfs(place, x, y, depth):
        if place[x][y] == 'P' and 1<= depth <= 2:
            return True
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<5 and 0<=ny<5:
                if not visited[nx][ny] and place[nx][ny] != 'X':
                    visited[nx][ny] = True
                    if dfs(place, nx, ny, depth+1):
                        return True
                    visited[nx][ny] = False
                    
    for place in places:
        flag = False
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    visited = [[False for _ in range(5)] for _ in range(5)]
                    visited[i][j] = True
                    #거리두기를 지키지 않고 있는 경우
                    if dfs(place, i, j, 0):
                        answer.append(0)
                        flag = True
                        break
            if flag:
                break
        if not flag:
            answer.append(1)
    return answer