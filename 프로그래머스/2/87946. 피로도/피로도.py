answer = -1
def solution(k, dungeons):
    n = len(dungeons)
    
    #탐험할 수 있는 최대 던전 수
    def dfs(depth, cost, visit):
        global answer
        answer = max(answer, depth)
        if depth == n:
            print(visit)
            return

        for i in range(n):
            #방문하지 않은 던전이라면
            if i not in visit and cost >= dungeons[i][0]:
                visit.append(i)
                cost -= dungeons[i][1]
                dfs(depth+1, cost, visit)
                visit.pop() 
                cost += dungeons[i][1]
                
    visit = []
    dfs(0, k, visit)
    return answer