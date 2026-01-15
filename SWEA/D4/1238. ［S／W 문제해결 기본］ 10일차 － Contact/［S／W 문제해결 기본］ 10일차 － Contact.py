def bfs(start):
    q = [(start, 0)]
    visited = [False] * 101
    last = []
    visited[start] = True
    while q:
        now, depth = q.pop(0)
        for v in graph[now]:
            if not visited[v]:
                q.append((v, depth+1))
                visited[v] = True
                last.append((v, depth+1))

    return last

for t in range(10):
    n, start = map(int, input().split())
    calls = list(map(int, input().split()))

    call_set = set()
    graph = [[] for _ in range(101)]
    for i in range(0, len(calls)-1, 2):
        if (calls[i], calls[i+1]) not in call_set:
            graph[calls[i]].append(calls[i+1])
            call_set.add((calls[i], calls[i+1]))

    result = sorted(bfs(start), key = lambda x: (-x[1], -x[0]))
    print("#%d %d" %(t+1, result[0][0]))


