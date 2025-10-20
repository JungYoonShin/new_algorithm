
#욱제가 트램펄린으로 최대한 많은 별똥별을 튕겨낼 때, 지구에 부딪히는 별똥별의 개수를 출력한다.

n, m, l, k = map(int, input().split())

stars = [list(map(int, input().split())) for _ in range(k)]

d = [[-l, -l], [0, -l], [0, 0], [-l, 0]]
answer = -1e9
for x1, y1 in stars:
    for x2, y2 in stars:
        cnt = 0
        for sx, sy in stars:
            if x1 <= sx <= x1 + l and y2 <= sy <= y2 + l:
                cnt += 1
        answer = max(answer, cnt)

print(k-answer)