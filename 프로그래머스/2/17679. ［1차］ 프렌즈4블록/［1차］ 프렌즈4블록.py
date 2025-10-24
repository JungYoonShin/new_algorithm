
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
def solution(m, n, board):
    board.reverse()
    field = [list(cols) for cols in zip(*board)]
    answer = 0

    while True:
        bomb = set()
        for row in range(n - 1):
            for col in range(m - 1):
                try:
                    if field[row][col] == field[row + 1][col] == field[row][col + 1] == field[row + 1][col + 1]:
                        bomb.update({(row, col), (row + 1, col), (row, col + 1), (row + 1, col + 1)})
                except:
                    break

        if not len(bomb):
            break

        for r, c in bomb:
            field[r][c] = ''
            answer += 1

        for row in range(n):
            field[row] = list(''.join(field[row]))

    return answer
