import math
def solution(n, k):
    answer = 0
    rev_base = ''
    
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    rev_base = rev_base[::-1]
    rev_base = rev_base.split('0')
    
    def isPrime(num):
        if num == 2:
            return True
        if num > 2:
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True
        return False
    
    for n in rev_base:
        if n != '' and isPrime(int(n)):
            answer += 1
    
    return answer