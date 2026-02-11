import sys

# 빠른 입력을 위해 사용
input = sys.stdin.readline

r, c, m = map(int, input().split())

# graph[x][y] = [속력, 방향, 크기]
graph = [[None for _ in range(c)] for _ in range(r)]

for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    graph[x-1][y-1] = [s, d, z]

dx = [0, -1, 1, 0, 0] # 1:위, 2:아래, 3:오른쪽, 4:왼쪽
dy = [0, 0, 0, 1, -1]

result = 0

# 1) 낚시왕이 오른쪽으로 한 칸씩 이동
for man_y in range(c):
    # 2) 해당 열에서 가장 땅에 가까운 상어 포획
    for x in range(r):
        if graph[x][man_y]:
            result += graph[x][man_y][2] # 크기 합산
            graph[x][man_y] = None
            break

    # 3) 상어 이동을 위한 새 격자판
    new_graph = [[None for _ in range(c)] for _ in range(r)]
    
    for x in range(r):
        for y in range(c):
            if graph[x][y]:
                s, d, z = graph[x][y]
                
                # 속력 최적화: 제자리로 돌아오는 주기(cycle) 제외
                if d <= 2: # 상하
                    move_s = s % ((r - 1) * 2) if r > 1 else 0
                else: # 좌우
                    move_s = s % ((c - 1) * 2) if c > 1 else 0
                
                nx, ny = x, y
                for _ in range(move_s):
                    # 벽에 부딪히면 방향 전환
                    if d == 1 and nx == 0: d = 2
                    elif d == 2 and nx == r - 1: d = 1
                    elif d == 3 and ny == c - 1: d = 4
                    elif d == 4 and ny == 0: d = 3
                    
                    nx += dx[d]
                    ny += dy[d]
                
                # 이동 후 위치에 상어가 이미 있다면 크기 비교
                if new_graph[nx][ny]:
                    if new_graph[nx][ny][2] < z:
                        new_graph[nx][ny] = [s, d, z]
                else:
                    new_graph[nx][ny] = [s, d, z]
    
    graph = new_graph

print(result)
