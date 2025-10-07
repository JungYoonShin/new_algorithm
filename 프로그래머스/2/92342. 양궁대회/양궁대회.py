def solution(n, info):
    answer = []
    
    
    #a=b=0일 경우 아무도 점수 가져가지 x, a=b일 경우 어피치가 점수 가져감
    #최종 점수 같을 경우 어피치 우승자
    #라이언이 가장 큰 점수차로 우승하기 위한 배열
    
    def dfs(depth, ryan, apeach, arrow):
        if depth == 11:
            if arrow > 0:
                ryan[10] += arrow
            ryan_total, apeach_total = 0, 0
            for i in range(11):
                if ryan[i] == apeach[i] == 0:
                    continue
                if ryan[i] > apeach[i]:
                    ryan_total += (10-i)
                else:
                    apeach_total += (10-i)
            
            if apeach_total < ryan_total:
                answer.append([ryan_total-apeach_total, ryan[:]])
                
            if arrow > 0:
                ryan[10] -= arrow
            
            return
        
        #해당 점수 따거나
        need = apeach[depth] + 1
        if arrow >= need:
            ryan[depth] = need
            dfs(depth+1, ryan, apeach, arrow-need)
            ryan[depth] = 0
        
        #헤당 점수 안 따거나
        dfs(depth+1, ryan, apeach, arrow)
    
    dfs(0, [0] * 11, info, n)
    if not answer:
        return [-1]
    else:
        answer.sort(key = lambda x: (x[0], x[1][::-1]), reverse=True)
    
    return answer[0][1]