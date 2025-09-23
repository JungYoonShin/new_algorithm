from collections import deque

def solution(board):
    n = len(board)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    INF = 1e9

    # graph[x][y][dir] = (x,y)에 dir 방향으로 들어왔을 때 최소 비용
    graph = [[[INF]*4 for _ in range(n)] for _ in range(n)]
    q = deque()

    # 시작점은 모든 방향 가능
    for i in range(4):
        graph[0][0][i] = 0
    q.append((0, 0, -1, 0))  # (x, y, 방향, 비용)

    answer = INF
    while q:
        a, b, d, cost = q.popleft()

        if a == n-1 and b == n-1:
            answer = min(answer, cost)
            continue

        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                if d == -1 or d == i:  
                    new_cost = cost + 100
                else: 
                    new_cost = cost + 600

                if new_cost < graph[nx][ny][i]:
                    graph[nx][ny][i] = new_cost
                    q.append((nx, ny, i, new_cost))

    return answer
