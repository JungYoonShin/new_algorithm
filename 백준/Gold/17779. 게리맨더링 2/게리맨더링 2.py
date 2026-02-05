import sys


def solve():
    N = int(sys.stdin.readline())
    city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    total_pop = sum(map(sum, city))
    min_diff = float('inf')

    for x in range(N):
        for y in range(N):
            for d1 in range(1, N):
                for d2 in range(1, N):
                    # 경계 조건 확인
                    if x + d1 + d2 >= N: continue
                    if y - d1 < 0 or y + d2 >= N: continue

                    # 각 구역 인구 저장
                    pop = [0] * 5
                    temp = [[0] * N for _ in range(N)]

                    # 5구역 경계선 표시
                    for i in range(d1 + 1):
                        temp[x + i][y - i] = 5
                        temp[x + d2 + i][y + d2 - i] = 5
                    for i in range(d2 + 1):
                        temp[x + i][y + i] = 5
                        temp[x + d1 + i][y - d1 + i] = 5

                    # 1구역
                    for r in range(x + d1):
                        for c in range(y + 1):
                            if temp[r][c] == 5: break
                            pop[0] += city[r][c]
                    # 2구역
                    for r in range(x + d2 + 1):
                        for c in range(N - 1, y, -1):
                            if temp[r][c] == 5: break
                            pop[1] += city[r][c]
                    # 3구역
                    for r in range(x + d1, N):
                        for c in range(y - d1 + d2):
                            if temp[r][c] == 5: break
                            pop[2] += city[r][c]
                    # 4구역
                    for r in range(x + d2 + 1, N):
                        for c in range(N - 1, y - d1 + d2 - 1, -1):
                            if temp[r][c] == 5: break
                            pop[3] += city[r][c]

                    pop[4] = total_pop - sum(pop[:4])
                    min_diff = min(min_diff, max(pop) - min(pop))

    print(min_diff)


solve()
