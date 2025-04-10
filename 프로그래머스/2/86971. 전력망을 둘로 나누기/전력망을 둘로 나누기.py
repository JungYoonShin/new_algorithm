def solution(n, wires):
    answer = 1e9  

    def dfs(start, visited):
        global cnt
        visited[start] = True
        for i in graph[start]:
            if not visited[i]:
                cnt += 1
                dfs(i, visited)
        return cnt

    for i in range(len(wires)):  
        temp_wires = wires[:]
        del temp_wires[i]

        # 그래프 초기화
        graph = [[] for _ in range(n + 1)]
        for a, b in temp_wires:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * (n + 1)
        
        global cnt
        cnt = 1  
        ss = dfs(a, visited)

        answer = min(answer, abs(ss - (n - ss)))

    return answer
