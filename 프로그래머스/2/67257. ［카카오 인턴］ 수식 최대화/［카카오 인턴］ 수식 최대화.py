import copy
from itertools import permutations
def solution(expression):
    answer = 0
    
    possible = list(permutations(['*', '-', '+'],  3))
    
    s = ''
    exp = []
    for e in expression:
        if e in ['*', '-', '+']:
            exp.append(s)
            exp.append(e)
            s = ''
        else:
            s += e
    exp.append(s)
    print(exp)
    
    for p in possible:
        temp = copy.deepcopy(exp)
        for i in range(len(p)):
            result = []
            j = 0
            while j < len(temp):
                if temp[j] == p[i]:
                    a = result.pop()
                    b = temp[j+1]
                    if temp[j] == '-':
                        result.append(int(a) - int(b))
                    
                    elif p[i] == '*':
                        result.append(int(a) * int(b))
                    else:
                        result.append(int(a) + int(b))
                    
                    j += 2
                else:
                    result.append(temp[j])
                    j += 1
                    
            temp = copy.deepcopy(result)
            
        answer = max(answer,abs(temp[0]))
    
    return answer