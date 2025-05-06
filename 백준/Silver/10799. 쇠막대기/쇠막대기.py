s = input().strip()  # 입력 받을 때 공백을 제거

stack = []
result = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if s[i-1] == '(':
            result += len(stack)
        else:
            result += 1

print(result)
