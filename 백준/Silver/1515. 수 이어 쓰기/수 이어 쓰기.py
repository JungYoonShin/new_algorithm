import sys
input=sys.stdin.readline

target = input().rstrip()
idx = 0
n = 1

while True:
    for ch in str(n):
        if idx < len(target) and ch == target[idx]:
            idx += 1
        if idx == len(target):
            print(n)
            exit()
    n += 1

