from itertools import combinations
from collections import defaultdict
def solution(relation):
    answer = []
    n = len(relation)
    
    for i in range(1, len(relation[0])+1):
        combis = list(combinations(range(len(relation[0])), i))
        
        for combi in combis:
            distinct = set()
            for re in relation:
                r = ''
                for c in combi:
                    r += re[c]
                distinct.add(r)
                
            #유일성 만족
            if len(distinct) == n:
                answer.append(combi)
    
    result = set()
    for a in answer:
        for b in answer:
            if set(a) != set(b) and set(a).issubset(set(b)):
                result.add(b)
    
    # print(set(answer), result)
    # print(set(answer) - result)
    return len(set(answer) - result)