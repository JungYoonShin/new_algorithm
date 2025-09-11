from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    n = len(queue1)
    half = (sum1+sum2) // 2
    
    while True:
        if sum1 == sum2:
            break
        
        if answer >= 3*n:
            answer = -1
            break
            
        #q2에서 원소 pop해야함
        elif sum1 < sum2:
            q2 = queue2.popleft()
            queue1.append(q2)
            answer += 1
            sum2 -= q2
            sum1 += q2
        
        #q1에서 원소 pop해야함
        else:
            q1 = queue1.popleft()
            queue2.append(q1)
            answer += 1
            sum1 -= q1
            sum2 += q1

    return answer