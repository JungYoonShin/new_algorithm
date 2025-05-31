from collections import defaultdict
def solution(clothes):
    answer = 1
    
    c = defaultdict(int)
    for clothe_name, clothe_type in clothes:
        c[clothe_type] +=1
    
    for i in c.keys():
        answer = answer * (c[i]+1)
    return answer-1