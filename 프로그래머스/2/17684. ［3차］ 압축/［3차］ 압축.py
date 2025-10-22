def solution(msg):
    answer = []

    dictionary = {}
    
    for i in range(26):
        dictionary[chr(65+i)] = i+1
    
    idx = 27
    while msg:
        for i, s in enumerate(msg):
            if msg[0:i+1] in dictionary:
                k = i+1
            else:
                break
                
        answer.append(dictionary[msg[0:k]])
        dictionary[msg[0:k+1]] = idx
        idx += 1
        msg = msg[k:]

    return answer