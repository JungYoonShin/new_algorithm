t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    # 양수
    if d > 0:
        for _ in range(d // 45):
            new_graph = [row[:] for row in graph]

            for i in range(n):
                new_graph[i][n//2] = graph[i][i]


            for i in range(n):
                new_graph[i][n-1-i] = graph[i][n//2]

            for i in range(n):
                new_graph[n//2][n-1-i] = graph[i][n-1-i]

            for i in range(n):
                new_graph[i][i] = graph[n//2][i]

            graph = new_graph
    else:
        for _ in range(abs(d) // 45):
            new_graph = [row[:] for row in graph]

            for i in range(n):
                new_graph[i][i] = graph[i][n//2]

            for i in range(n):
                new_graph[n//2][i] = graph[i][i]

            for i in range(n):
                new_graph[n-1-i][i] = graph[n//2][i]

            for i in range(n):
                new_graph[n-1-i][n//2] = graph[n-1-i][i]


            graph = new_graph


    for i in range(n):
        print(*graph[i], sep=" ")