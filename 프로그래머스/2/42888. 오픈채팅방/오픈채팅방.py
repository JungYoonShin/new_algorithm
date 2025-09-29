from collections import defaultdict
def solution(records):
    answer = []
    
    name = defaultdict(int)
    
    for record in records:
        s = record.split(" ")
        if s[0] == 'Leave':
            answer.append([s[1], "나갔습니다."])
        elif s[0] == 'Enter':
            name[s[1]] = s[2]
            answer.append([s[1], "들어왔습니다."])
        else:
            name[s[1]] = s[2]
        
    for i in range(len(answer)):
        answer[i] = name[answer[i][0]] + "님이 " + answer[i][1]
    return answer