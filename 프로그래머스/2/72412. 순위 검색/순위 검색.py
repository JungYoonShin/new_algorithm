from itertools import combinations
from bisect import bisect_left
from collections import defaultdict
def solution(infos, query):
    answer = []
    
    status = defaultdict(list)
    for info in infos:
        #4자리 중 0~4개가 -가 들어갈 수 있다.
        for i in range(5):
            places = list(combinations(range(4), i))
            for place in places:
                new = info.split(" ")
                score = new[4]
                new = new[0:4]
                for p in place:
                    new[p] = '-'
                status[''.join(new)].append(int(score))
                
    for k in status.keys():
        status[k].sort()
    
    for q in query:
        q = q.replace(' and ', ' ')
        q = q.split(' ')
        score = int(q[4])
        q = ''.join(q[0:4])
        answer.append(len(status[q]) - bisect_left(status[q], score))
    return answer