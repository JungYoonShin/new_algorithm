def solution(plans):
    answer = []
    
    #무조건 새로운 과제를 시작할 시각 -> 기존 과제 stop, 새로운 과제 start
    #과제 끝 => 멈춰둔 과제 start, 여러개면 가장 최근에 멈춘 과제
    n = len(plans)
    for i in range(n):
        now = plans[i]
        time = now[1].split(":")
        plans[i][1] = int(time[0]) * 60 + int(time[1])
        plans[i][2] = int(plans[i][2])
    
    plans.sort(key = lambda x: x[1])
    print(plans)
    idx = 0
    stop = []
    
    while True:
        if len(answer) == n or idx > n-1:
            break
        now = plans[idx]
        time = now[1]
        playtime = now[2]

        if idx < n-1:
            #이번 과제를 끝내는 시간이 다음 과제 시작 시각보다 작고 멈춰둔 과제 있다면 실행
            next_time = plans[idx+1][1]
            if time + playtime == next_time:
                answer.append(now[0])
            elif time + playtime < next_time:
                answer.append(now[0])
                rest = next_time - (time+playtime)
                if stop:
                    while rest and stop:
                        name, p = stop.pop()
                        if rest == p:
                            answer.append(name)
                            break
                        elif rest < p:
                            stop.append([name, p-rest])
                            break
                        else:
                            answer.append(name)
                        
                        rest -= p
            else:
                stop.append([now[0], playtime-(next_time - time)])
        
        else:
            answer.append(now[0])
        idx += 1
    

    for a, b in stop[::-1]:
        answer.append(a)
            
    return answer