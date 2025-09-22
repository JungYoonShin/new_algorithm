import heapq
from collections import defaultdict
def solution(jobs):    
    time = 0
    
    dict_jobs = defaultdict(list)
    for i, job in enumerate(jobs):
        req_time, cost_time = job
        dict_jobs[req_time].append([cost_time, i])
    
    q = []
    disk = [] #요청시각이랑 작업 종료시각 저장
    answer = []
    while True:
        #jobs가 비어있으면 작업 다 완료한 것(break)
        if len(disk) != 0 and len(answer) == len(jobs):
            break
        
        #disk가 안비어잇고, 지금이 작업 종료시각이라면 디스크 비우기
        if len(disk) != 0 and time == disk[-1][1]:
            disk.pop()
        
        #jobs 중에 지금 시각과 요청 시각작업이 겹치는게 있다 -> 큐에 넣음
        for cost, i in dict_jobs[time]:
            heapq.heappush(q, [cost, time, i])
        
        
        #현재 작업 중이 아니라면, 큐에서 꺼냄
        if len(disk) == 0 and q:
            c_time, r_time, idx = heapq.heappop(q) #소요시간, 요청시각, 번호
            disk.append([r_time, time+c_time])
            answer.append([idx, r_time, time+c_time])
        
        time += 1
    
    
    total = sum(a[2]-a[1] for a in answer)
    
    return total//len(jobs)