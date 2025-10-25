def solution(info, edges):
    #각 노드를 방문하면서 모을 수 있는 양은 최대 몇 마리
    answer = 1
    n = len(info)
    
    
    def dfs(now, wolf, sheep):
        nonlocal answer
        if sheep <= wolf:
            return
        else:
            answer = max(answer, sheep)
        
        for v, e in edges:
            if visited[v] and not visited[e]:
                #다음 방문할 곳이 늑대라면
                visited[e] = True
                if info[e] == 1:
                    dfs(e, wolf+1, sheep)
                else:
                    dfs(e, wolf, sheep+1)
                visited[e] = False
    
    visited = [False] * n
    visited[0] = True
    dfs(0, 0, 1)
    # print(answer)
    return answer