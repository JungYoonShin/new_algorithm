#블록은 상하좌우로 이동이 가능하며, 같은 숫자를 가진 두 블록이 충돌하면 하나의 블록으로 합쳐짐
#이미 합쳐진 블록은 또 다른 블록과 합쳐질 수 없다.
#이동하려는 쪽의 칸이 먼저 합쳐진다.
#최소 5번 이동해서 만들 수 있는 가장 큰 블록의 값
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(d, graph):
    merge = [[False] * n for _ in range(n)]

    # 충돌 감지해서 합치기
    if d == 0:
        a = range(1, n)
        b = range(n)

    elif d == 1:
        a = range(n-2, -1, -1)
        b = range(n)

    elif d == 2:
        a = range(n)
        b = range(1, n)
    else:
        a = range(n)
        b = range(n-2, -1, -1)

    for i in a:
        for j in b:
            if graph[i][j] == 0:
                continue

            x, y = i, j
            while True:
                nx, ny = x + dx[d], y + dy[d]

                if 0<=nx<n and 0<=ny<n:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y]
                        graph[x][y] = 0
                        x, y = nx, ny

                    else:
                        if graph[nx][ny] == graph[x][y] and not merge[nx][ny]:
                            graph[nx][ny] *= 2
                            graph[x][y] = 0
                            merge[nx][ny] = True
                        break
                else:
                    break
    return graph

answer = 0
def tries(cnt, g):
    global answer
    if cnt == 5:
        answer = max(answer, max(map(max, g)))
        return
    
    for d in range(4):
        new = [row[:] for row in g]
        moved = move(d, new)
        tries(cnt+1, moved)

tries(0, graph)
print(answer)

