import math
from collections import defaultdict
def solution(fees, records):
    answer = []
    timetable = defaultdict(list)
    
    for record in records:
        time, num, in_or_out = record.split(" ")
        timetable[num].append(time)
    
    
    for a, b in timetable.items():
        if not len(b) % 2 == 0:
            timetable[a].append('23:59')
    
    total = defaultdict(int)
    
    for a, b in timetable.items():
        times = 0
        for i in range(1, len(b), 2):
            in_hour, in_minute = map(int, b[i-1].split(":"))
            out_hour, out_minute = map(int, b[i].split(":"))
            
            times += (out_hour * 60 + out_minute) - (in_hour * 60 + in_minute)
        total[a] = times
            
    for num, time in total.items():
        if time <= fees[0]:
            cost = fees[1]
        else: 
            cost = fees[1] + math.ceil((time-fees[0])/fees[2]) * fees[3]
        total[num] = cost
        
    answer = [[num, cost] for num, cost in total.items()]
    answer.sort(key = lambda x: x[0])

    return [x[1] for x in answer]