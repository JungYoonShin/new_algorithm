from collections import deque

def solution(board):
    n = len(board)
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n and board[x][y] == 0

    def move(lx, ly, rx, ry, dist, visited, q):
        # 평행이동
        for i in range(4):
            nlx, nly = lx + dx[i], ly + dy[i]
            nrx, nry = rx + dx[i], ry + dy[i]
            
            if is_valid(nlx, nly) and is_valid(nrx, nry):
                new_pos = tuple(sorted([(nlx, nly), (nrx, nry)]))
                if new_pos not in visited:
                    visited.add(new_pos)
                    q.append([list(new_pos), dist + 1])
        
        # 가로 상태 회전
        if lx == rx:
            # 왼쪽 블록 기준 회전 (위/아래)
            if is_valid(lx - 1, ly) and is_valid(lx - 1, ly + 1):
                new_pos = tuple(sorted([(lx, ly), (lx - 1, ly)]))
                if new_pos not in visited:
                    visited.add(new_pos)
                    q.append([list(new_pos), dist + 1])
            if is_valid(lx + 1, ly) and is_valid(lx + 1, ly + 1):
                new_pos = tuple(sorted([(lx, ly), (lx + 1, ly)]))
                if new_pos not in visited:
                    visited.add(new_pos)
                    q.append([list(new_pos), dist + 1])

            # 오른쪽 블록 기준 회전 (위/아래)
            if is_valid(rx - 1, ry) and is_valid(rx - 1, ry - 1):
                new_pos = tuple(sorted([(rx - 1, ry), (rx, ry)]))
                if new_pos not in visited:
                    visited.add(new_pos)
                    q.append([list(new_pos), dist + 1])
            if is_valid(rx + 1, ry) and is_valid(rx + 1, ry - 1):
                new_pos = tuple(sorted([(rx + 1, ry), (rx, ry)]))
                if new_pos not in visited:
                    visited.add(new_pos)
                    q.append([list(new_pos), dist + 1])
        
        # 세로 상태 회전
        elif ly == ry:
            # 위쪽 블록 기준 회전 (왼/오)
            if is_valid(lx, ly - 1) and is_valid(rx, ry - 1):
                new_pos = tuple(sorted([(lx, ly - 1), (lx, ly)]))
                if new_pos not in visited:
                    visited.add(new_pos)
                    q.append([list(new_pos), dist + 1])
            if is_valid(lx, ly + 1) and is_valid(rx, ry + 1):
                new_pos = tuple(sorted([(lx, ly), (lx, ly + 1)]))
                if new_pos not in visited:
                    visited.add(new_pos)
                    q.append([list(new_pos), dist + 1])

            # 아래쪽 블록 기준 회전 (왼/오)
            if is_valid(lx, ly - 1) and is_valid(rx, ry - 1):
                new_pos = tuple(sorted([(rx, ry - 1), (rx, ry)]))
                if new_pos not in visited:
                    visited.add(new_pos)
                    q.append([list(new_pos), dist + 1])
            if is_valid(lx, ly + 1) and is_valid(rx, ry + 1):
                new_pos = tuple(sorted([(rx, ry), (rx, ry + 1)]))
                if new_pos not in visited:
                    visited.add(new_pos)
                    q.append([list(new_pos), dist + 1])

    def bfs():
        q = deque([[((0, 0), (0, 1)), 0]])
        visited = set([((0, 0), (0, 1))])
        while q:
            (pos1, pos2), dist = q.popleft()
            if pos1 == (n - 1, n - 1) or pos2 == (n - 1, n - 1):
                return dist
            lx, ly = pos1
            rx, ry = pos2
            move(lx, ly, rx, ry, dist, visited, q)
        return 0
    
    return bfs()
