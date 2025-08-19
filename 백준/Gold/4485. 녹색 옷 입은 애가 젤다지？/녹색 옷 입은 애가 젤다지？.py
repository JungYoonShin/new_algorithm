import sys
input = sys.stdin.readline
import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def djk():
    answer = [[1e9 for _ in range(n)] for _ in range(n)]
    answer[0][0] = 0
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))

    while q:
        dist, x, y = heapq.heappop(q)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n:
                if dist + graph[nx][ny] < answer[nx][ny]:
                    answer[nx][ny] = dist + graph[nx][ny]
                    heapq.heappush(q, (answer[nx][ny], nx, ny))

    print(f'Problem {count}: {answer[n-1][n-1]}')
count = 1
while True:
    n = int(input())

    if n == 0:
        break
    visited = [[False for _ in range(n)] for _ in range(n)]
    graph = [list(map(int, input().split())) for _ in range(n)]
    djk()
    count += 1
