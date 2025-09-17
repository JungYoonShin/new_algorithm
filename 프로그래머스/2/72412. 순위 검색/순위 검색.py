from collections import defaultdict
from itertools import product
from bisect import bisect_left

def solution(infos, query):
    answer = []
    db = defaultdict(list)
    possible = list(product([0,1], repeat=4))
    
    for info in infos:
        data = info.split()
        for p in possible:
            temp = data[:]
            for i in range(4):
                if p[i] == 1:
                    temp[i] = '-'
            key = " ".join(temp[:4])
            db[key].append(int(data[4]))

    for key in db:
        db[key].sort()
    
    for q in query:
        q = q.replace(" and ", " ")
        l, j, y, f, s = q.split()
        key = " ".join([l, j, y, f])
        score_list = db[key]
        idx = bisect_left(score_list, int(s))
        answer.append(len(score_list) - idx)
    
    return answer
