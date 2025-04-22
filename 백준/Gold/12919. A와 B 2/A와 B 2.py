import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

ans = 0
def dfs(t):
    global ans

    if t == s:
        ans = 1
        return

    if len(t) == 0:
        return

    if t[-1] == 'A':
        dfs(t[:-1])

    if t[0] == 'B':
        dfs(t[1:][::-1])

dfs(t)
print(ans)
