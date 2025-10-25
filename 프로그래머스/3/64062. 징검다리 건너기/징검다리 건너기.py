def solution(stones, k):
    answer = -1e9
    start = 1
    end = 200000000
    n = len(stones)
    
    while start<=end:
        friend = (start+end)//2
        # print(friend, new_stone)
        cnt = 0
        for stone in stones:
            if stone - friend <= 0:
                cnt += 1
                if cnt >= k:
                    break
            else:
                cnt = 0
                    
        if cnt <= k-1:
            answer = max(answer, friend)
            start = friend + 1
        else:
            end = friend-1
            
    return answer+1
