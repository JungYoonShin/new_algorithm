def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()
    bus_time = {}
    start_time = 9 * 60
    for i in range(n):
        bus_time[start_time + t * i] = []
    
    for time in timetable:
        hour, minute = time.split(":")
        total_time = int(hour) * 60 + int(minute)
        for bus in bus_time.keys():
            if total_time <= bus and len(bus_time[bus]) < m:
                bus_time[bus].append(total_time)
                break
    
    last_bus_time = list(bus_time)[-1]
    if len(bus_time[last_bus_time]) < m:
        return f"{last_bus_time//60:02d}:{last_bus_time%60:02d}"
    else:
        t = bus_time[last_bus_time][-1] - 1
        return f"{t//60:02d}:{t%60:02d}"
    
    return answer