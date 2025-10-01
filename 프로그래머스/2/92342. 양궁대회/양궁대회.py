from itertools import product
def solution(n, infos):
    answer = []
    
    
    #무조건 지거나 비기는 경우에는 -1을 return한다.
    #해당 과녁 점수를 먹거나 안 먹거나
    
    def dfs(arrow, ryan, apeach, idx):
        
        if idx == 11:
            if arrow > 0:
                ryan[10] += arrow
            ryan_score, apeach_score = 0, 0
            for i in range(11):
                if apeach[i] < ryan[i]:
                    ryan_score += (10-i)
                elif apeach[i] > 0:
                    apeach_score += (10-i)

            
            if apeach_score < ryan_score:
                answer.append([ryan_score-apeach_score, ryan[:]])
            
            if arrow > 0:
                ryan[10] -= arrow
            return
                    
        #해당 점수를 먹거나
        need = apeach[idx] + 1
        if arrow >= need:
            ryan[idx] = need
            dfs(arrow - need, ryan, apeach, idx+1)
            ryan[idx] = 0

        
        #안 먹거나
        dfs(arrow, ryan, apeach, idx+1)
    
    dfs(n, [0]*11, infos, 0)
    if not answer:
        return [-1]
    else:
        answer.sort(key = lambda x: (x[0], list(reversed(x[1]))), reverse= True)
    
    return answer[0][1]