from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    
    appear = defaultdict(int)
    #각각의 코스 종류에 대해서 조합 구하기
    for order in orders:
        for c in course:
            combis = list(combinations(sorted(order), c))
        
            for combi in combis:
                appear[combi] += 1
    
    result = [[] for _ in range(11)]
    for k in appear.keys():
        result[len(k)].append([k, appear[k]])

        
    for c in course:
        result[c].sort(key = lambda x: -x[1])
        if result[c] and result[c][0][1] > 1:
            max_appear = result[c][0][1]

        for a in result[c]:
            if a[1] == max_appear:
                answer.append(''.join(a[0]))
    
    
    return sorted(answer)