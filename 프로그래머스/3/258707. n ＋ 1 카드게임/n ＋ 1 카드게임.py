from collections import deque

answer = -1
def solution(coin, cards):
    global answer
    n = len(cards)
    
    def play_round(get_card, remain, available, rounds, coins):
        global answer
        
        answer = max(rounds, answer)
        
        if len(remain) > 0:
            available.append(remain.popleft())
            available.append(remain.popleft())
        else:
            return 
        
        if len(get_card) >= 2:
            for c1 in get_card:
                if n+1-c1 in get_card:
                    get_card.remove(c1)
                    get_card.remove(n+1-c1)
                    play_round(get_card, remain, available, rounds+1, coins)
                    return 
        
        if len(get_card) > 0 and len(available) > 0 and coins > 0:
            for c1 in get_card:
                if n+1-c1 in available:
                    available.remove(n+1-c1)
                    get_card.remove(c1)
                    play_round(get_card, remain, available, rounds+1, coins-1)
                    return 
        
        if len(available) >= 2 and coins >= 2:
            for c1 in available:
                if n+1-c1 in available:
                    available.remove(n+1-c1)
                    available.remove(c1)
                    play_round(get_card, remain, available, rounds+1, coins-2)
                    return 
    
    
    play_round(cards[0:n//3], deque(cards[n//3:]), [], 1, coin)
    
    return answer