from collections import defaultdict
def solution(gems):
    answer = [0, 1e9]
    
    diamond = len(set(gems))
    n = len(gems)
    end = 0
    status = defaultdict(int)
    
    
    for start in range(n):
        while end < n and len(status) < diamond:
            status[gems[end]] += 1
            end += 1
            
        if len(status) == diamond and end-1-start < answer[1] - answer[0]:
            answer = [start+1, end]
        
        status[gems[start]] -= 1
        if status[gems[start]] == 0:
            del status[gems[start]]
        start += 1
            
    return answer