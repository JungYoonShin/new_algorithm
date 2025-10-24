def solution(n, info):
    answer = []
    
    # a<b여야 라이언이 점수를 가져간다. a=b=0이면 아무도 점수 안 가져감 
    #최종 점수가 더 높은 선수를 우승자로 결정합니다. 단, 최종 점수가 같을 경우 어피치를 우승자로 결정
    # 라이언이 가장 큰 점수차이로 우승할 수 있는 방법(여러가지면 가장 낮은 점수를 더 많이 맞힌 경우), 이길 수 없다면 [-1] return 
    
    def dfs(ryan, arrow, depth):
        if depth == 11:
            #화살이 남아 있다면
            if arrow > 0:
                ryan[10] += arrow
            ryan_score, apeach_score = 0, 0
            for i in range(11):
                if ryan[i] > info[i]:
                    ryan_score += (10-i)
                elif info[i] > 0:
                    apeach_score += (10-i)
            
            if ryan_score > apeach_score:
                answer.append([ryan_score - apeach_score, ryan[:]])
                
            if arrow > 0:
                ryan[10] -= arrow
            return
                    
        #해당 과녁 점수를 가져가거나(화살이 남아있어야 함)
        if info[depth] < arrow:
            need_arrow = info[depth] + 1
            ryan[depth] = need_arrow
            dfs(ryan, arrow-need_arrow, depth+1)
            ryan[depth] = 0
        
        dfs(ryan, arrow, depth+1)
    
    dfs([0] * 11, n, 0)
    
    if not answer:
        return [-1]
    else:
        answer.sort(key = lambda x: (x[0], x[1][::-1]), reverse=True)
        return answer[0][1]
