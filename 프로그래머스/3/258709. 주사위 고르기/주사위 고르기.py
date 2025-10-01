from itertools import combinations, product
from bisect import bisect_left
def solution(dice):
    answer = []
    n = len(dice)
    combis = set(combinations(range(n), n//2))
    
    for combi in combis:
        b_combi = []
        for i in range(n):
            if i not in combi:
                b_combi.append(i)
        
        #A가 가질 수 있는 모든 합 구하기
        a_dice = list(product([0, 1, 2, 3, 4, 5], repeat = n//2))
        a_value = []
        for a in a_dice:
            total = 0
            for i in range(n//2):
                total += dice[combi[i]][a[i]]
            a_value.append(total)
        
        #B가 가질 수 있는 모든 합 구하기
        b_dice = list(product([0, 1, 2, 3, 4, 5], repeat = n//2))
        b_value = []
        for b in b_dice:
            total = 0
            for i in range(n//2):
                total += dice[b_combi[i]][b[i]]
            b_value.append(total)
        
        b_value.sort()
        a_win = 0
        for a in a_value:
            idx = bisect_left(b_value, a)
            a_win += idx
        
        if answer:
            if answer[1] < a_win:
                answer = [combi, a_win]
        else:
            answer = [combi, a_win]
            
    return [x+1 for x in answer[0]]