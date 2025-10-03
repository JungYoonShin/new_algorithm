def solution(info, edges):
    answer = -1e9
    
    #양 <= 늑대 이면 안됨, 최대한 많은 수의 양을 모아서 돌아와야함
    n = len(info)
    graph = [[] for _ in range(n)]
    for edge in edges:
        a, b = edge
        graph[a].append(b)
    
    def dfs(now, sheep, wolf, can_visit):
        nonlocal answer
        answer = max(answer, sheep)

        can_visit.update(graph[now][:])
        if sheep <= wolf:
            return

        for v in can_visit:
            s, w = sheep, wolf
            if info[v] == 1:
                w += 1
            else:
                s += 1
            if s <= w:
                continue

            next_visit = set(can_visit)
            next_visit.remove(v)
            dfs(v, s, w, next_visit)

    
    dfs(0, 1, 0, set())
    print(answer)
    return answer