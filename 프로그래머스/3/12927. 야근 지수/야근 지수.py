import heapq
def solution(n, works):
    answer = 0
    
    if sum(works) <= n:
        return 0
    
    works = [-w for w in works]
    heapq.heapify(works)
    
    for i in range(n):
        w = heapq.heappop(works)
        w += 1
        heapq.heappush(works, w)
        
    for w in works:
        answer += abs(w) ** 2

    return answer