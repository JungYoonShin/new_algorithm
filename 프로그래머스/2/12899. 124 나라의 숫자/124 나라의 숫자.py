def solution(n):
    answer = ''
    
    s = ['0', '1', '2', '4']
    while n>0:
        if n % 3 == 0:
            answer += '4'
            n = (n-1) // 3
        else:
            answer += s[n%3]
            n = n // 3

    return answer[::-1]