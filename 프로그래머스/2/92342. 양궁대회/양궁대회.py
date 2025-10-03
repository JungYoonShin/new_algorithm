def solution(n, info):
    answer = []
    
    # a=b일 경우 어피치가 점수 가져감
    # a=b=0이면 아무도 안가져감
    # 라이언이 가장 큰 점수 차이로 우승할 수 있는 방법 return 
    
    def dfs(idx, ryan, apeach, arrow):
        if idx == 11:
            if arrow > 0:
                ryan[10] += arrow
            apeach_score, ryan_score = 0, 0
            for i in range(11):
                if apeach[i] == 0 and ryan[i] == 0:
                    continue
                if apeach[i] < ryan[i]:
                    ryan_score += (10-i)
                else:
                    apeach_score += (10-i)
            
            if ryan_score > apeach_score:
                answer.append([ryan_score-apeach_score, ryan[:]])
            
            if arrow > 0:
                ryan[10] -= arrow
                
            return
        
        #해당 점수 먹거나
        need = apeach[idx] + 1
        if arrow >= need:
            ryan[idx] = need
            dfs(idx+1, ryan, apeach, arrow-need)
            ryan[idx] = 0
            
        
        #안 먹거나
        dfs(idx+1, ryan, apeach, arrow)
    
    dfs(0, [0]*11, info, n)
    
    if not answer:
        return [-1]
    else:
        answer.sort(key = lambda x: (x[0], x[1][::-1]), reverse=True)
    
    return answer[0][1]