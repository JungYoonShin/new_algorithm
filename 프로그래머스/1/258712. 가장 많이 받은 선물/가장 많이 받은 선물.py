from collections import defaultdict
from itertools import combinations
def solution(friends, gifts):
    answer = defaultdict(int)
    
    #구하고자 하는 것: 다음달에 가장 많은 선물을 받는 친구가 받을 선물의 수
    
    name = {}
    gift_rank = defaultdict(int)
    for i, friend in enumerate(friends):
        name[friend] = i
        
    n = len(friends)
    gift_status = [[0 for _ in range(n)] for _ in range(n)]
    
    for gift in gifts:
        give, take = gift.split(" ")
        gift_status[name[give]][name[take]] += 1
        gift_rank[give] += 1
        gift_rank[take] -= 1
    
    
    for a, b in list(combinations(friends, 2)):
        
        #선물을 주고 받을 적이 없거나 주고 받은 수가 같다면 선물 지수 큰 사람이 하나 받는다.
        if (gift_status[name[a]][name[b]] == 0 and gift_status[name[b]][name[a]] == 0) or (
        gift_status[name[a]][name[b]] == gift_status[name[b]][name[a]]):
            if gift_rank[a] > gift_rank[b]:
                answer[a] += 1
            elif gift_rank[a] < gift_rank[b]:
                answer[b] += 1
        else:
            if gift_status[name[a]][name[b]] < gift_status[name[b]][name[a]]:
                answer[b] += 1
            else:
                answer[a] += 1
    
    if not answer:
        return 0
    
    answer = list(answer.items())
    answer.sort(key = lambda x: -x[1])
    return answer[0][1]