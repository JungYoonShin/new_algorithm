#if 전체 종이가 모두 같은 색 x =? n/2, n/2로 나눈다.
#언제까지? 각각 나눈 부분이 모두 같은 색으로 칠해져 있거나 더 이상 나눌 수 없을 때까지

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0

def devide(x, y, size):
    global white, blue
    for i in range(x, x + size):
        for j in range(y, y+size):
            if graph[i][j] != graph[x][y]:
                devide(x, y, size//2)
                devide(x, y+ size//2, size//2)
                devide(x+size//2, y, size//2)
                devide(x+size//2, y+size//2, size//2)
                return

    if graph[x][y] == 0:
        white += 1
    else:
        blue += 1
devide(0, 0, n)
print(white, blue, sep = '\n')