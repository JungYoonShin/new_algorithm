from collections import defaultdict
def solution(record):
    answer = []
    dict = defaultdict(list)
    
    for r in record:
        status = r.split()
        if status[0] != 'Leave':
            dict[status[1]] = status[2]
    
    for r in record:
        status = r.split()
        if status[0] == 'Enter':
            answer.append(dict[status[1]] + "님이 들어왔습니다.")
        elif status[0] == 'Leave':
            answer.append(dict[status[1]] + "님이 나갔습니다.")
            
    
    return answer