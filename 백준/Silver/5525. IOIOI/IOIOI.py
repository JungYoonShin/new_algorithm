n = int(input())
m = int(input())
ss = input()

result = []
cnt = 0
i = 0
answer = 0
while i < m-2:
    if ss[i:i+3] == 'IOI':
        cnt += 1
        i += 2
    else:
        if cnt:
            result.append(cnt)
        cnt = 0
        i += 1

if cnt:
    result.append(cnt)

for a in result:
    if a >= n:
        answer += a - n + 1
        
print(answer)