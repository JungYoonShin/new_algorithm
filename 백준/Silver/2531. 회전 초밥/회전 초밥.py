import sys
input = sys.stdin.readline


n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]

result = []
belt = sushi[:k]
result = 0
for i in range(n):
    belt.pop(0)
    belt.append(sushi[(i+k)%n])
    result = max(result, len(set(belt + [c])))
    if result == d:
        break
print(result)