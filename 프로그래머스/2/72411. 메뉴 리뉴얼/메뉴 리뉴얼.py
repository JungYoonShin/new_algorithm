from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    
    for n in course:
        status = defaultdict(int)
        for order in orders:
            dishes = list(combinations(sorted(order), n))
            dishes.sort()
            for dish in dishes:
                status[''.join(dish)] += 1
        
        cnt = []
        for k in status.keys():
            cnt.append([k, status[k]])
        cnt.sort(key = lambda x: -x[1])
        if cnt:
            max_cnt = cnt[0][1]
        if max_cnt >= 2:
            
            for c in cnt:
                if c[1] == max_cnt:
                    answer.append(c[0])
                else:
                    break
    answer.sort()
    # print(answer)
    return answer