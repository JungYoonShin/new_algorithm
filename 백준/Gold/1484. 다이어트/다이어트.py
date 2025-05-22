import sys
input=sys.stdin.readline

g = int(input())

start = 1
end = 1

result = []
while start + end <= g:
    if start**2 - end**2 == g:
        result.append(start)
        start += 1
    elif start**2 - end**2 < g:
        start +=1
    elif start**2 - end**2 > g:
        end += 1

if len(result) == 0:
    print(-1)
else:
    print(*result, sep='\n')