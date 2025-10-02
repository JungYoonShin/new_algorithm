def solution(alp, cop, problems):
    answer = 0
    
    #주어진 모든 문제들을 풀 수 있는 알고력과 코딩력을 얻는 최단시간
    #[필요한 알고력, 필요한 코딩력, 증가하는 알고력, 증가하는 코딩력, 걸리는 시간]
    
    max_alp = max([x[0] for x in problems]) 
    max_cop = max([x[1] for x in problems]) 
    
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    dp = [[1e9 for _ in range(max_cop+1)] for _ in range(max_alp+1)]
    dp[alp][cop] = 0
    
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            # 공부하기
            if i+1 <= max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1, dp[i+1][j-1] + 1)
            if j+1 <= max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1, dp[i-1][j+1] + 1)
                
            for problem in problems:
                if problem[0] <= i and problem[1] <= j:
                    ni = min(max_alp, i + problem[2])
                    nj = min(max_cop, j + problem[3])
                    dp[ni][nj] = min(dp[ni][nj], dp[i][j] + problem[4])
                            
    
    return dp[max_alp][max_cop]