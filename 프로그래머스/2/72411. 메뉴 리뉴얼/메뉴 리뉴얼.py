from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    
    combi = defaultdict(int)
    
    for order in orders:
        order = list(order)
        for i in range(2, len(order)+1):
            order_combi = list(combinations(sorted(order), i))
            for c in order_combi:
                combi[''.join(c)] += 1
    
    for cnt in course:
        result = [] 
        for k in combi.keys():
            if len(k) == cnt:
                if result and combi[k] >= result[-1][1] and combi[k] >= 2:
                    result.append([k, combi[k]])
                elif not result and combi[k] >= 2:
                    result.append([k, combi[k]])
        
        result.sort(key = lambda x: -x[1])
        if result:
            max_value = result[0][1]
        
        for r in result:
            if r[1] == max_value:
                answer.append(r[0])
    answer.sort()
    return answer