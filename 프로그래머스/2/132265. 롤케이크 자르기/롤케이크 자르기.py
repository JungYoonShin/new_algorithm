from collections import Counter
def solution(topping):
    answer = 0
    n = len(topping)
    
    
    # for i in range(1, n-1):
    #     if len(set(topping[0:i])) == len(set(topping[i:])):
    #         answer += 1
    
    a = Counter(topping)
    b = set()
    for i in topping:
        a[i] -= 1
        b.add(i)
        
        if a[i] == 0:
            a.pop(i)
        
        if len(a) == len(b):
            answer+=1
    
    return answer