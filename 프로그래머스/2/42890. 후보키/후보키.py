from itertools import combinations
def solution(relation):
    answer = []
    key = set()
    column = len(relation[0])
    all = []
    
    #후보키가 1개일때부터 8개일때까지 구한다.
    for i in range(1, column+1):
        all.append(list(combinations(list(range(column)), i)))
    
    # if set([0, 1]).issubset((0, 1, 2)):
    #     print(3)
    
    for a in all:
        for possible in a:
            appear = set()
            for idx, tuple in enumerate(relation):
                s = ''
                for p in possible:
                    s += relation[idx][p]
                
                appear.add(s)
            
            if len(appear) == len(relation):
                key.add(possible)
    
    key = list(key)
    key.sort(key = lambda x: len(x))
    
    answer.append(key[0])
    print(key)
    print(answer)
    
    for k in key:
        for a in answer:
            if set(a).issubset(set(k)):
                break
        else:
            answer.append(k)
            
    
    return len(answer)