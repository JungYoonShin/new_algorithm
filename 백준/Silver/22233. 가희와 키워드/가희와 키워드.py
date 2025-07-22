import sys

input = sys.stdin.readline

n, m = map(int, input().split())
memo_keyword = set(input().rstrip() for _ in range(n))

for _ in range(m):
    word = input().rstrip().split(',')
    for w in word:
        if w in memo_keyword:
            memo_keyword.remove(w)
    print(len(memo_keyword))