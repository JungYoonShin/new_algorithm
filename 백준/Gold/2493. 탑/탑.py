n = int(input())
tops = list(map(int, input().split()))
top_dict = {}
for i, top in enumerate(tops):
    top_dict[top] = i

stack = [tops[0]]
answer = [0] * (n)
for i in range(1, n):
    while stack and stack[-1] < tops[i]:
        stack.pop()
    if stack:
        answer[i] = top_dict[stack[-1]]+1
    stack.append(tops[i])

print(*answer)
