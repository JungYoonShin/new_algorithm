def solution(s):
    answer = True
    
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if stack and stack[-1] == ')':
                return False
            elif not stack:
                return False
            elif stack and stack[-1] == '(': 
                stack.pop()
                
    if stack:
        return False
    
    return True