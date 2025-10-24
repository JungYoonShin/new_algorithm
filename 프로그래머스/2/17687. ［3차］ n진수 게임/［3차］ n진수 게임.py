def solution(n, t, m, p):
    answer = ''
    
    alphabet = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    number = ''
    
    for i in range(t*m+1):
        num = i
        s = []
        while True:
            a, b = divmod(num, n)
            num = a
            s.append(b)
            if a == 0:
                break
        s = s[::-1]
        for k in range(len(s)):
            if 10<=s[k]<=15:
                s[k] = alphabet[s[k]]
            else:
                s[k] = str(s[k])
                
        number += ''.join(s)
    
    for i in range(p-1, t*m, m):
        answer += number[i]
                
    return answer