import copy
def solution(info, edges):
    answer = -1e9
    
    n = len(info)
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
    
    def dfs(now, sheep, wolf, can_visit):
        nonlocal answer
        answer = max(answer, sheep)

        if sheep <= wolf:
            return
        
        can_visit.extend(graph[now][:])
        for v in can_visit:
            s, w = sheep, wolf
            if info[v] == 1:
                w += 1
            else:
                s += 1
            if s <= w:
                continue

            next_visit = copy.deepcopy(can_visit)
            next_visit.remove(v)
            dfs(v, s, w, next_visit)


    dfs(0, 1, 0, [])
    return answer
