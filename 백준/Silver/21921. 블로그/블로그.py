import sys
input=sys.stdin.readline

n, x = map(int, input().split())
visit = list(map(int, input().split()))
#누적합
s = [0] * (n)
s[0] = sum(visit[0:x])
for i in range(1, n-x+1):
    s[i] = s[i-1] - visit[i-1] + visit[i+x-1]

result = max(s)
if result == 0:
    print("SAD")
else:
    print(result)
    print(s.count(result))
