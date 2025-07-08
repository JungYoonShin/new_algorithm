def solution(s):
    answer = ''
    num = s.split()
    num = [int(n) for n in num]
    num.sort()
    
    return str(num[0]) + " " + str(num[-1])