import math
def solution(brown, yellow):
    answer = []
    
    
    total = brown + yellow
    for i in range(1, int(math.sqrt(total))+1):
        if total % i == 0:
            a = total // i
            b = total // a
            
            if (a-2) * (b-2) == yellow:
                if 2*a +2*(b-2) == brown:
                    return [a, b]
    
    return answer