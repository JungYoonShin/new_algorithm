from itertools import permutations

def solution(numbers):
    answer = sorted(numbers, key = lambda x : str(x)*3, reverse=True)
    
    answer = ''.join(map(str, answer))
    
    if int(answer) == 0:
        return '0'
    else:
        return answer