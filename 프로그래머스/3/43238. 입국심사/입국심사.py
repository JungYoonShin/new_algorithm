def solution(n, times):
    answer = 0
    
    start = 0
    end = max(times) * n
    
    #최소시간 구하기
    while start <= end:
        mid = (start + end) // 2
        
        #시간 동안 심사할 수 있는 사람 수
        people = 0
        for time in times:
            people += (mid//time)
        
        if people >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
        
    return answer