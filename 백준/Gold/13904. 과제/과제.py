import sys
input = sys.stdin.readline

n= int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
graph.sort(key=lambda x: -x[1])

max_day = max(d for d, _ in graph)

assigned = [0] * (max_day+1)
total = 0
for d, w in graph:
    for day in range(d, 0, -1):
        if not assigned[day]:
            assigned[day] = 1
            total += w
            break
print(total)