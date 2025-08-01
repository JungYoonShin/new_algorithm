from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    
    dic = defaultdict(list)
    sum_time = defaultdict(int)
    for record in records:
        time, number, out_or_in = record.split()
        number = int(number)
        hour, minute = map(int, time.split(":"))
        
        #입차기록이 있다면 출차시각 - 입차시각
        if dic[number]:
            in_hour, in_minute = map(int, dic[number][0].split(":"))
            total = (hour * 60 + minute)-(in_hour * 60 + in_minute) 
            sum_time[number] += total
            dic[number].pop()
            
        #입차기록이 없다면 입차시각 저장
        else:
            dic[number].append(time)
    
    for k in dic.keys():
        if dic[k]:
            in_hour, in_minute = map(int, dic[k][0].split(":"))
            sum_time[k] += (23 * 60 + 59)-(in_hour * 60 + in_minute) 
            
    basic_time, basic_fee, time, fee = fees
    sum_time = dict(sorted(sum_time.items()))
    
    for k in sum_time.keys():
        if sum_time[k] > basic_time:
            total_fee = basic_fee + math.ceil((sum_time[k]-basic_time)/time) * fee
            answer.append(total_fee)
        else:
            answer.append(basic_fee)
    
    return answer