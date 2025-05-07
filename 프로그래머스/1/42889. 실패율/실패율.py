from collections import defaultdict
def solution(N, stages):
    answer = []
    cnt = defaultdict(int)
    
    for stage in stages:
        cnt[stage] += 1
    
    result = []
    for i in range(1, N+1):
        #스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수
        yet = cnt[i]
        #스테이지에 도달한 플레이어 수
        complete = 0
        for j in range(i, N+2):
            complete += cnt[j]
        if complete == 0:
            result.append((i, 0))
        else:
            result.append((i, yet/complete))
    
    result.sort(key=lambda x: (-x[1], x[0]))
    return [x[0] for x in result]