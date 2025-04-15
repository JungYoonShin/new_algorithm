import math
def solution(brown, yellow):
    answer = []
    
    total = brown + yellow
    
    for a in range(1, total+1):
        if total % a == 0:
            b = total // a
            if a >= b:
                if 2*a + 2*b - 4 == brown and (a-2) * (b-2) == yellow:
                    return [a, b]
                    
                    