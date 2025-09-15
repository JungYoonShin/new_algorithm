def solution(n, tops):
    answer = 0
    
    #방법2로 채우는 경우
    dp2 = [0] * (n)
    ndp2 = [0] * (n)
    
    #방법2로 채우는 경우
    dp2[0] = 1
    
    #방법2는 사용하지 않는 경우
    if tops[0] == 1:
        ndp2[0] = 3
    else:
        ndp2[0] = 2
    
    for i in range(1, n):
        #뿔이 있다면
        if tops[i] == 1:
            ndp2[i] = (dp2[i-1] * 2 + ndp2[i-1] * 3) % 10007
        else:
            ndp2[i] = (dp2[i-1] * 1 + ndp2[i-1] * 2) % 10007
        dp2[i] = (dp2[i-1] + ndp2[i-1]) % 10007
    
    return (ndp2[n-1] + dp2[n-1]) % 10007