from collections import defaultdict
def solution(user_id, banned_id):
    answer = 0
    
    ban = defaultdict(list)
    for i in range(len(banned_id)):
        for user in user_id:
            flag = True
            if len(user) == len(banned_id[i]):
                for j in range(len(banned_id[i])):
                    if banned_id[i][j] != '*':
                        if user[j] != banned_id[i][j]:
                            flag = False
                            break
            else:
                flag = False
                        
            if flag:
                ban[i].append(user)
    
    result = set()
    def dfs(idx, chosen):
        if idx == len(banned_id):
            result.add(frozenset(chosen))
            return
        
        for user in ban[idx]:
            if user not in chosen:
                chosen.append(user)
                dfs(idx+1, chosen)
                chosen.remove(user)
    
    dfs(0, [])
    return len(result)