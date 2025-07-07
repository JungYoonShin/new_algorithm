import sys
input = sys.stdin.readline

n = int(input())
dasom = int(input())
li = [int(input()) for _ in range(n-1)]
cnt = 0

if (n==1):
  pass
else:
  while dasom <= max(li):
    dasom += 1
    cnt += 1
    li[li.index(max(li))] -= 1

print(cnt)