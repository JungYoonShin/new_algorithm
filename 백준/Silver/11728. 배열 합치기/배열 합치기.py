import sys
input=sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

pointer_a = 0
pointer_b = 0

result = []
while pointer_a < n and pointer_b < m:
    if A[pointer_a] < B[pointer_b]:
        result.append(A[pointer_a])
        pointer_a += 1
    else:
        result.append(B[pointer_b])
        pointer_b += 1

if pointer_a < n:
    result += (A[pointer_a:])
elif pointer_b < m:
    result += (B[pointer_b:])

print(*result)