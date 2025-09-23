import sys

input = sys.stdin.readline

# 남쪽 보고 있음 처음에 .은 이동가능 #은 벽임
# 모든 칸을 다님, 처음에 어떤칸에 있는지 모름

start_x, start_y = 0, 0

dx = [1, 0, -1, 0] #남 -> 서 -> 북 -> 동(오른쪽으로 회전시)
dy = [0, -1, 0, 1]

graph = set()
graph.add((start_x, start_y))
d = 0

n = int(input())
course = input().rstrip()

for c in course:
    if c == 'R':
        d = (d+1) % 4

    elif c == 'L':
        d = (d-1) % 4

    else:
        start_x += dx[d]
        start_y += dy[d]
        graph.add((start_x, start_y))

graph = list(graph)
min_x = abs(min(x[0] for x in graph))
min_y = abs(min(x[1] for x in graph))
graph = [(x + min_x, y + min_y) for x, y in graph]
max_x = max(x for x, _ in graph)
max_y = max(y for _, y in graph)

new_graph = [['#' for _ in range(max_y+1)] for _ in range(max_x+1)]

for x, y in graph:
    new_graph[x][y] = '.'

for row in new_graph:
    print("".join(row))