from itertools import permutations
def solution(user_id, banned_id):
    answer = 0
    
    user_combi = list(permutations(user_id, len(banned_id)))
    
    def check(i, user):
        if len(user) != len(banned_id[i]):
            return False
        
        for j in range(len(user)):
            if banned_id[i][j] == '*':
                continue
            if user[j] != banned_id[i][j]:
                return False
        return True
            
    result = set()
    for user in user_combi:
        possible = set()
        for i in range(len(user)):
            if check(i, user[i]):
                possible.add(user[i])
            else:
                break
        else:
            if possible not in result:
                result.add(frozenset(possible))
    
    return len(result)