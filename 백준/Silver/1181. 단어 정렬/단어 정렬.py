import sys

input = sys.stdin.readline

n = int(input())
alphabet = set()
for i in range(n):
    alphabet.add(input().rstrip())

new = list(alphabet)
new.sort(key= lambda x : (len(x), x))
print(*new, sep="\n")