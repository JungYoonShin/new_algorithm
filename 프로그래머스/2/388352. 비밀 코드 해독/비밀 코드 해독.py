from itertools import combinations

def solution(n, q, ans):
    answer = 0
    f = list(combinations(list(range(1, n+1)), 5))
    
    for g, cnt in zip(q, ans):
        f = [code for code in f if len(set(g) & set(code)) == cnt]

    return len(f)
