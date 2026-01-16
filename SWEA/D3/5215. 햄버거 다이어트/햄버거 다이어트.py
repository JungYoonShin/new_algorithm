#정해진 칼로리 이하의 조합 중에서 민기가 가장 선호하는 햄버거를 조합해주는 프로그램
#같은 재료 여러번 x


t = int(input())

def combi(cnt, food, now):
    global result
    if len(food) == cnt:
        results.append(food[:])
        return

    for i in range(now+1, n):
        food.append(i)
        combi(cnt, food, i)
        food.pop()


for test in range(t):
    answer = -1e9
    n, l = map(int, input().split()) #재료의수, 제한 칼로리
    food = [list(map(int, input().split())) for _ in range(n)] #점수, 칼로리

    #재료의 개수는 1~n개 가능하다
    for i in range(1, n+1):
        results = []
        combi(i, [], -1)

        for result in results:
            taste = 0
            calories = 0
            for idx in result:
                taste += food[idx][0]
                calories += food[idx][1]
                if calories > l:
                    break
            else:
                answer = max(answer, taste)

    print("#%d %d" %(test+1, answer))




