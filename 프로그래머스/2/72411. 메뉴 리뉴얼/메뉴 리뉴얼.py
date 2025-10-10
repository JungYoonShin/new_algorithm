from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    
    for k in course:
        status = []
        for order in orders:
            for li in list(combinations(order, k)):
                status.append(''.join(sorted(li)))
        
        cnt = Counter(status).most_common()
        for menu, count in cnt:
            if count >= 2 and count == cnt[0][1]:
                answer.append(menu)
    return sorted(answer)