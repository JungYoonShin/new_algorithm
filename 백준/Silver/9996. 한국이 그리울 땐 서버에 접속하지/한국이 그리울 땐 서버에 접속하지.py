import sys
input = sys.stdin.readline

n = int(input())
pattern = input().rstrip()
pre, post = pattern.split('*')

for _ in range(n):
    word = input().rstrip()
    if len(word) < len(pre) + len(post):
        print("NE")
    elif word.startswith(pre) and word.endswith(post):
        print("DA")
    else:
        print("NE")
