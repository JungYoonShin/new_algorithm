from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(information, query):
    answer = []
    dic = defaultdict(list)
    
    for info in information:
        infos = info.split()
        key = infos[:-1]
        score = int(infos[-1])
        
        for i in range(5):
            case = list(combinations([0,1,2,3], i))
            for c in case:
                temp = key[:]
                for idx in c:
                    temp[idx] = '-'
                          
                dic[' '.join(temp)].append(score)
    
    for k in dic:
        dic[k].sort()
        
    for q in query:
        q = q.replace(' and', '').split()
        score = int(q[-1])
        q = ' '.join(q[:-1])
        if q in dic.keys():
            id = bisect_left(dic[q], score)
            answer.append(len(dic[q]) - id)
        else:
            answer.append(0)
    
    return answer
