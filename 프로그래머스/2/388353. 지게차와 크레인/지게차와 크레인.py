from collections import deque

def solution(storage, requests):
    answer = 0
    n = len(storage)
    m = len(storage[0])
    
    storage = list(map(list, storage))
    new_storage = [[0 for _ in range(m+2)] for _ in range(n+2)]
    for i in range(n):
        for j in range(m):
            new_storage[i+1][j+1] = storage[i][j]
    
    storage = new_storage
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def out_side():
        q = deque([(0, 0)])
        visited = [[False for _ in range(m+2)] for _ in range(n+2)]
        visited[0][0] = True
        
        while q:
            a, b = q.popleft()
            
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                
                if 0<=nx<n+2 and 0<=ny<m+2:
                    if not visited[nx][ny]:
                        if storage[nx][ny] == -1:
                            storage[nx][ny] = 0
                            q.append((nx, ny))
                            visited[nx][ny] = True
                        elif storage[nx][ny] == 0:
                            q.append((nx, ny))
                            visited[nx][ny] = True
    
    def get_out(request):
        alphabet = request[0]
        if len(request) == 1:
            remove = []
            for i in range(1, n+1):
                for j in range(1, m+1):
                    if storage[i][j] == alphabet:
                        for k in range(4):
                            nx = i + dx[k]
                            ny = j + dy[k]
                            if storage[nx][ny] == 0:
                                remove.append((i, j))
                                break
            for a, b in remove:
                storage[a][b] = 0
            out_side()
                
        elif len(request) == 2:
            for i in range(1, n+1):
                for j in range(1, m+1):
                    if storage[i][j] == alphabet:
                        storage[i][j] = -1
            
            out_side()
        
    
    for request in requests:
        get_out(request)
        # print(*storage, sep= "\n")
        # print()
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            if storage[i][j] != 0 and storage[i][j] != -1:
                answer += 1
    
    return answer