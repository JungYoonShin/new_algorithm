from itertools import combinations
def solution(relation):
    answer = 0
    n = len(relation[0]) #컬럼 개수
    answer = []
    
    #후보키가 될 수 있는 크기(1 ~ 컬럼개수)
    for i in range(1, n+1):
        for possible in list(combinations(list(range(n)), i)):
            #최소성을 만족하기 위한 조건
            if any(set(a).issubset(possible) for a in answer):
                continue
            
            student = set()
            for row in relation:
                s = ''
                for p in possible:
                    s += row[p]
                
                student.add(s)
            
            if len(student) == len(relation):
                answer.append(possible)
            
    return len(answer)