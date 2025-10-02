from itertools import product
def solution(users, emoticons):
    answer = [0, 0]
    
    #1. 가입자 최대, 2. 판매액 최대
    #모든 할인 경우의 수 (10, 20, 30, 40) 다 해봄
    #이모티콘 할인률 다름
    sales = list(product([10, 20, 30, 40], repeat = len(emoticons)))
    for sale in sales:
        total = [0, 0]
        for user in users:
            buy = 0
            for i in range(len(sale)):
                #할인율이 기준보다 높으면 구매함
                if sale[i] >= user[0]:
                    buy += emoticons[i] * (100 - sale[i]) // 100
            #구매 비용이 크면 가입함
            if buy >= user[1]:
                total[0] += 1
            else:
                total[1] += buy
        
        answer = max(total, answer)
        
    return answer