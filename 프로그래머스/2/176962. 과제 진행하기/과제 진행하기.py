from collections import deque
def solution(plans):
    answer = []
    
    finish = []
    stop = []
    
    for i in range(len(plans)):
        h, m = plans[i][1].split(":")
        plans[i][1] = int(h) * 60 + int(m)
        plans[i][2] = int(plans[i][2])
    
    plans.sort(key = lambda x: x[1])
        
    for i in range(len(plans)):
        if i + 1 < len(plans):
            start = plans[i][1]
            play_time = plans[i][2]
            
            next_start = plans[i+1][1]
            
            between = next_start - (start+play_time)

            #이번 과제를 다 수행하고도 다음 과제까지 까지 시간이 남을 경우
            if between > 0:
                finish.append(plans[i][0])
                while stop:
                    a, b, c = stop.pop()
                    if c - between == 0:
                        finish.append(a)
                        break
                    elif c - between < 0:
                        finish.append(a)
                        between -= c
                    else:
                        stop.append([a, b, c-between])
                        break
                        
            elif between == 0:
                finish.append(plans[i][0])
                
            #중간에 멈춰야 하는 경우
            else:
                stop.append([plans[i][0], plans[i][1], plans[i][2] - (next_start - start)])
        else:
            finish.append(plans[i][0])
            while stop:
                a, b, c = stop.pop()
                finish.append(a)
        
    
    return finish