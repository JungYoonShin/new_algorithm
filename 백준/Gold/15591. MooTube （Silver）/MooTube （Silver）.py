import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n, q = map(int, input().split())
graph = defaultdict(list)

for _ in range(n - 1):
    a, b, usado = map(int, input().split())
    graph[a].append((b, usado))
    graph[b].append((a, usado))

def bfs(k, v):
    visited = [0] * (n + 1)
    visited[v] = 1
    result = 0
    queue = deque([(v, 1e9)])
    while queue:
        v, usado = queue.popleft()
        for n_v, n_usado in graph[v]:
            n_usado = min(usado, n_usado)
            if n_usado >= k and not visited[n_v]:
                result += 1
                queue.append((n_v, n_usado))
                visited[n_v] = 1

    return result

for _ in range(q):
    k, v = map(int, input().split())
    print(bfs(k, v))
