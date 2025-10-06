from collections import defaultdict
def solution(gems):
    answer = []
    
    find_gem = defaultdict(int)
    start = 0
    n = len(gems)
    gem_type = len(set(gems))
    answer = [0, n-1]
    unique = 0
    end = 0
    
    for start in range(n):
        while unique < gem_type and end < n:
            find_gem[gems[end]] += 1
            if find_gem[gems[end]] == 1:
                unique += 1
            end += 1
        
        if unique == gem_type:
            if end-1-start < answer[1] - answer[0]:
                answer= [start, end-1]
        
        find_gem[gems[start]] -=1
        if find_gem[gems[start]] == 0:
            unique -= 1
    
    return [answer[0]+1, answer[1]+1]