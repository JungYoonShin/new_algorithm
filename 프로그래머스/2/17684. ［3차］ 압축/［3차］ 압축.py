def solution(msg):
    answer = []
    index = {}
    
    for i in range(65, 91):
        index[chr(i)] = i-64
    
    last = 27
    start = 0
    while True:
        for i in range(len(msg), start, -1):
            if msg[start:i] in index:
                answer.append(index[msg[start:i]])
                
                index[msg[start:i+1]] = last
                last += 1
                
                start = i
                break
        
        if start >= len(msg):
            break
        
    return answer
