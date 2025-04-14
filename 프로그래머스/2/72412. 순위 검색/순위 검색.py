from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    
    info_list = defaultdict(list)
    for infos in info:
        a = infos.split()
        need = a[:-1]
        score = int(a[-1])
        
        for n in range(5): # '-'가 들어갈 수 있는 개수 (0~4)
            for combi in combinations(range(4), n): #'-'가 들어갈 수 있는 위치
                temp = need[:]
                for idx in combi:
                    temp[idx] = '-'
                info_list[' '.join(temp)].append(score)
    
    for k in info_list.values():
        k.sort()


    #이분 탐색
    for q in query:
        s = q.replace("and", "")
        s = s.split()
        score = int(s[-1])
        find = info_list[' '.join(s[:-1])]
        
        idx = bisect_left(find, score)

        answer.append(len(find) - idx)
        
    return answer