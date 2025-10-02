def solution(edges):
    answer = [0, 0, 0, 0]
    
    #들어오느게 없고 나가는 것만 많으면 정점
    
    status = [[0, 0] for _ in range(1000000)] #나가는것, 들어오는 것
    
    for edge in edges:
        out, come = edge
        status[out][0] += 1
        status[come][1] += 1
        
    for i, (o, c) in enumerate(status):
        #정점 
        if o >= 2 and c == 0:
            answer[0] = i
            e = i
        
        #막대 그래프 
        elif o == 0 and c >= 1:
            answer[2] += 1
                
        #8자 그래프 
        elif o >= 2 and c >= 2:
            answer[3] += 1
    
    answer[1] = status[e][0] - (answer[2] + answer[3])
        
    
    return answer