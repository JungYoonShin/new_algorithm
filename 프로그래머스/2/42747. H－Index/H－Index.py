from bisect import bisect_left
def solution(citations):
    answer = 0
    
    citations.sort()
    print(citations)
    answer = -1e9
    for i in range(max(citations)+1):
        if i <= len(citations) - bisect_left(citations, i):
            answer = max(answer, i)
        
    
    return answer