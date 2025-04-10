def solution(word):
    answer = []
    
    alphabet = ['A', 'E', 'I', 'O', 'U']
    
    s= ''
    
    def dfs(s):
        nonlocal answer
        if len(s) == 5:
            return
        for i in range(5):
            answer.append(s + alphabet[i])
            dfs(s + alphabet[i])
    dfs('')
    return answer.index(word) +1

