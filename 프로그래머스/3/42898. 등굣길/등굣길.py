def solution(m, n, puddles):
    answer = 0
    
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if i==0 and j == 0:
                continue
            #위가 없음
            if i==0:
                dp[i][j] = dp[i][j-1]
            #왼쪽이 없음
            if j==0:
                dp[i][j] = dp[i-1][j]
                
            if [j+1, i+1] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1])  % 1000000007
    
    
    return dp[n-1][m-1]