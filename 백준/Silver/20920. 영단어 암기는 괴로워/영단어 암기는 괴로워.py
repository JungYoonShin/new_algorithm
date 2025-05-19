import sys
from collections import defaultdict
input=sys.stdin.readline

# 자주 나오는 단어일수록 앞에 배치한다.
# 해당 단어의 길이가 길수록 앞에 배치한다.
# 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다
# + 길이가 m이상인 것만 외움

n, m = map(int, input().split())
alphabet = [input().rstrip() for _ in range(n)]

new = defaultdict(int)
for s in alphabet:
    if len(s) < m:
        continue
    new[s] += 1

s = list(new)
s.sort(key=lambda x: (-new[x], -len(x), x))
print(*s, sep="\n")