from collections import deque
def solution(storage, requests):
    answer = 0
    
    #알파벳 하나 -> 접근 가능한 컨테이너(4면 중 적어도 1면이 외부와 연결된 컨테이너)만 꺼낸다.
    #알파벳 두개 -> 알파벳에 해당하는 모든 컨테이너 꺼낸다. 
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(storage)
    m = len(storage[0])
    storage = list(map(list, storage))
    new_storage = [[0 for _ in range(m+2)] for _ in range(n+2)]
    for i in range(n):
        for j in range(m):
            new_storage[i+1][j+1] = storage[i][j]

    storage = new_storage
    def bfs(alphabet):
        q = deque([(0, 0)])
        visited = [[False for _ in range(m+2)] for _ in range(n+2)]
        visited[0][0] = True
        
        while q:
            a, b = q.popleft()
                
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                
                if 0<=nx<n+2 and 0<=ny<m+2:
                    if storage[nx][ny] == alphabet:
                        outside.append((nx, ny))
                    if not visited[nx][ny] and storage[nx][ny] == 0:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        
    for request in requests:
        alphabet = request[0]
        outside = []
        if len(request) == 1:
            bfs(alphabet)
            for a, b in outside:
                storage[a][b] = 0
            
        
        else:
            for i in range(1, n+1):
                for j in range(1, m+1):
                    if storage[i][j] == alphabet:
                        storage[i][j] = 0
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if storage[i][j] != 0:
                answer += 1
            
    return answer