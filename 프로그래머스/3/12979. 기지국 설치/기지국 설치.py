def solution(n, stations, w):
    answer = 0

    #추가로 증설해야하는 기지국 개수의 최소값
    location = []
    for i in range(1, len(stations)):
        location.append(stations[i]-w-(stations[i-1]+w)-1)
    
    location.append(stations[0]-w-1) 
    location.append(n-(stations[-1]+w))
    
    for l in location:
        if l > 0:
            if l % (w*2+1) == 0:
                answer += l // (w*2+1)
            else:
                answer += l // (w*2+1) + 1
        
    return answer