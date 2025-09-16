def solution(n, t, m, timetable):
    answer = ''
    
    #아직 넉넉하다면 버스 시각 맞춰서, 안넉넉하면 젤 마지막 애보다 1분 빨리
    start = 9 * 60
    
    arrive = {start: []}
    for i in range(n-1):
        start += t
        arrive[start] = []
    
    timetable.sort()
        
    for time in timetable:
        hour, minute = map(int, time.split(":"))
        for k in arrive.keys():
            if hour == 23 and minute == 59:
                continue
            else:
                if (hour*60+minute) <= k and len(arrive[k]) < m:
                    arrive[k].append(hour*60+minute)
                    break
    
    last_time = list(arrive.keys())[-1]
    print(arrive)
    
    if len(arrive[last_time]) < m:
        hour = last_time // 60
        minute = last_time % 60
    else:
        hour = (arrive[last_time][-1]-1) // 60
        minute = (arrive[last_time][-1]-1) % 60
    
    hour, minute = str(hour), str(minute)
    
    hour = hour.zfill(2)
    minute = minute.zfill(2)
    
    return f"{hour}:{minute}"