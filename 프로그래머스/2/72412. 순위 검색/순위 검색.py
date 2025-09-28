import copy
from bisect import bisect_left
from itertools import combinations
from collections import defaultdict
def solution(infos, query):
    answer = []
    
    all_info = defaultdict(list)
    for info in infos:
        q = info.split(" ")
        for x in range(5):
            #- 등장은 0부터 4번가능
            cases = list(combinations([0, 1, 2, 3], x))
            for case in cases:
                temp_q = copy.deepcopy(q)
                for c in case:
                    temp_q[c] = '-'
            
                all_info[''.join(temp_q[0:4])].append(int(q[-1]))
        
    for info in all_info.keys():
        all_info[info].sort()
        
    for q in query:
        q = q.replace(' and ' , '')
        q = q.split(' ')
        score = int(q[-1])
        idx = bisect_left(all_info[q[0]], score)
        answer.append(len(all_info[q[0]]) - idx)

    return answer