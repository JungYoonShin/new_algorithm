from collections import deque
def solution(n, m, x, y, r, c, k):
    answer = ''
    
    dir = [[1, 0, 'd'], [0, -1, 'l'], [0, 1, 'r'], [-1, 0, 'u']] #d, l, r, u 순으로 탐색
    
    x -= 1
    y -= 1
    r -= 1
    c -= 1
    def bfs(a, b):
        q = deque([(a, b, 0, [])])
        
        while q:
            x, y, depth, move = q.popleft()
            
            if depth == k and (x == r and y == c):
                return move
    
            for i in range(4):
                nx = x + dir[i][0]
                ny = y + dir[i][1]
                
                if 0<=nx<n and 0<=ny<m:
                    if abs(nx-r) + abs(ny-c) > k-(depth+1):
                        continue
                    q.append((nx, ny, depth+1, move+[dir[i][2]]))
                    break

            
                
    answer = bfs(x, y)
    if answer == None:
        return "impossible"
    else:
        return ''.join(answer)