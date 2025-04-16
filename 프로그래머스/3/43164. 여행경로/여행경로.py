def solution(tickets):
    answer = []
    answer_list= []
    
    visited = [False] * len(tickets)
    def dfs(start):
        if len(answer) == len(tickets) + 1:
            answer_list.append(answer[:])
            return
        
        for i, ticket in enumerate(tickets):
            now, to_go = ticket
            if now == start and not visited[i]:
                visited[i] = True
                answer.append(to_go)

                dfs(to_go)
                visited[i] = False
                answer.pop()
        return answer_list
    
    answer.append("ICN")
    dfs("ICN")
    answer_list.sort()
    
    return answer_list[0]