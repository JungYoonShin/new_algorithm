
stack = []
answer = []
n = int(input())
nums = [int(input()) for _ in range(n)]

start = 1
idx = 0
for i in range(n*2):
    if start > n+1:
        print("NO")
        break
    if not stack or stack[-1] != nums[idx]:
        stack.append(start)
        start += 1
        answer.append("+")
    elif stack and stack[-1] == nums[idx]:
        idx += 1
        stack.pop()
        answer.append("-")
else:
    print(*answer, sep="\n")