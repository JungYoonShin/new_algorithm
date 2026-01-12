def solution(plans):
    answer = []
    
    plans.sort(key = lambda x : x[1])
    print(plans)
    for idx, (name, start, playtime) in enumerate(plans):
        h, m = map(int, plans[idx][1].split(":"))
        plans[idx][1] = h * 60 + m
        plans[idx][2] = int(plans[idx][2])
    
    stop = []
    finish = []

    idx = 0
    now = plans[0][1]

    
    while True:
        if idx == len(plans) - 1:
            answer.append(plans[idx][0])
            while stop:
                answer.append(stop.pop()[0])
            break

        name, start, remain = plans[idx]
        next_start = plans[idx + 1][1]
            
        # 현재 과제 끝나는 시각
        end_time = now + remain
        
        #새로 시작해야하는 과제가 등장한다면 
        if next_start < end_time:
            remain -= (next_start- now)
            stop.append((name, remain))
            now = next_start
            idx += 1
        
        
        else:
            #다음 과제 시작 전까지 현재 과제를 끝낼 수 있는 경우
            answer.append(name)
            now = end_time
            gap = next_start - end_time
            
            while stop and gap > 0:
                s_name, s_remain = stop.pop()
                if s_remain <= gap:
                    now += s_remain
                    gap -= s_remain
                    answer.append(s_name)
                else:
                    stop.append((s_name, s_remain - gap))
                    now += gap
                    gap = 0
            
            
            now = next_start
            idx += 1
                    
                    
        
        
            
        
            
            
            
        
        
    
    
    
    
    return answer