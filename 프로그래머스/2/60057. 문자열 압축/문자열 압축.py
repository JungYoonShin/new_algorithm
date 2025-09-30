def solution(s):
    answer = len(s)
    
    #반복되는 가능한 횟수는 1 ~ len(s) - 1
    for i in range(1, len(s)//2+1):
        word = ''
        j = 0
        cnt = 0
        last = s[0:i]
        for j in range(0, len(s), i):
            #이전이랑 같으면 
            if last == s[j:j+i]:
                cnt += 1
            #이전이랑 다르면
            else:
                if cnt == 1:
                    word += last
                else: 
                    word += str(cnt) + last
                cnt = 1
                last = s[j:j+i]
        
        if cnt == 1:
            word += last
        else:
            word += str(cnt) + last
        answer = min(answer, len(word))
    return answer