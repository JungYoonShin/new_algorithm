import copy
def solution(stones, k):
    answer = 0
    
    #0이 연달아 나오는 구간의 길이가 k이상이면 안된다.
    left = 1
    right = 200000000
    while left <= right:
        mid = (left+right) // 2
        temp = stones.copy()
        cnt = 0
        for stone in temp:
            stone -= mid
            if stone <= 0:
                cnt += 1
            else:
                cnt = 0
            
            if cnt >= k:
                break
        
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid

    return answer+1