from itertools import permutations
def solution(user_id, banned_id):
    answer = 0
    
    can = [[] for _ in range(len(banned_id)+1)] 
    
    def canbe(user_tuple, banned_id):
        for u, b in zip(user_tuple, banned_id):
            if len(u) != len(b):
                return False
            for i in range(len(u)):
                if b[i] != '*' and u[i] != b[i]:
                    return False
        return True

    
    user_permutation = list(permutations(user_id, len(banned_id)))
    
    ban_set = []
    
    for user in user_permutation:
        if canbe(user, banned_id):
            if set(user) not in ban_set:
                ban_set.append(set(user))    
    
    return len(ban_set)