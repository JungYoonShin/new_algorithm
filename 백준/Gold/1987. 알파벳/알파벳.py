import sys
sys.setrecursionlimit(10**4)
input=sys.stdin.readline

r, c = map(int, input().split())
alphabet = []
for _ in range(r):
    alphabet.append(list(input().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_count = 0
def dfs(x, y, depth):
    global max_count
    max_count = max(max_count, depth)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<r and 0<=ny<c:
            if alphabet[nx][ny] not in alphas:
                alphas.add(alphabet[nx][ny])
                dfs(nx, ny, depth + 1)
                alphas.remove(alphabet[nx][ny])

alphas = set()
alphas.add(alphabet[0][0])
dfs(0,0,1)
print(max_count)

