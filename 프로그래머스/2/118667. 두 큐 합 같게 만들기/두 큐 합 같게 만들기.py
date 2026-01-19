from collections import deque
def solution(queue1, queue2):
    answer = -2
    
    sum_1 = sum(queue1)
    sum_2 = sum(queue2)
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    cnt = 0
    while True:
        if sum_1 == sum_2:
            break
        
        if sum_1 < sum_2:
            top = queue2[0]
            queue2.popleft()
            queue1.append(top)
            sum_1 += top
            sum_2 -= top
        
        elif sum_1 > sum_2:
            top = queue1[0]
            queue1.popleft()
            queue2.append(top)
            sum_2 += top
            sum_1 -= top
            
            
        cnt += 1
        
        if cnt > (len(queue1) + len(queue2)) * 2:
            answer = -1
            break
    
    if answer == -1:
        return -1
    else:
        return cnt
    