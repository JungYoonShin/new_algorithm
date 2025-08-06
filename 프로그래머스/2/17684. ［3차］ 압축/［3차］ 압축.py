def solution(msg):
    answer = []

    dict = {}
    
    for i in range(65, 91):
        dict[chr(i)] = i-64
    
    last = 27
    
    while msg:
            
        s = ''
        for i in range(len(msg)):
            if s + msg[i] in dict.keys():
                s += msg[i]
            else:
                break
                
        answer.append(dict[s])
        if i < len(msg):
            dict[s + msg[i]] = last
            last += 1

        msg = msg[len(s):]
    
    return answer