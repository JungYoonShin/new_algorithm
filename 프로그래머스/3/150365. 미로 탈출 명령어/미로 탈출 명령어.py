from collections import deque
import copy
def solution(n, m, x, y, r, c, k):
    answer = ''
    
    x -=1 
    y -= 1
    r -= 1
    c -= 1
    
    #이동거리 총 k여야함, 그리고 같은 격자 2번 이상 방문 가능, 모든 경로중 문자열 사전 순으로 가장 빠른 경로
    
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    def bfs(start_x, start_y):
        all_move = []

        q = deque([(start_x, start_y, 0, "")])
        
        while q:
            a, b, depth, move = q.popleft()
            
            if depth == k:
                if a==r and b==c:
                    move = move.replace('0', "d").replace('1', "l").replace('2', "r").replace('3', "u")
                    return move
            
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                
                if 0<=nx<n and 0<=ny<m:
                    if abs(nx - r) + abs(ny - c) > k - (depth + 1):
                        continue
                    q.append((nx, ny, depth+1, move+str(i)))
                    break
    
    result = bfs(x, y)
    if not result:
        return "impossible"
    
    return result