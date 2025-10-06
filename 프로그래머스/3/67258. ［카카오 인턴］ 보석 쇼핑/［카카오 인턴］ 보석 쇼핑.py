from collections import defaultdict

def solution(gems):
    gem_type = len(set(gems))
    n = len(gems)
    
    gem_cnt = defaultdict(int)
    unique = 0
    answer = (0, n - 1)
    end = 0

    for start in range(n):
        while end < n and unique < gem_type:
            gem_cnt[gems[end]] += 1
            if gem_cnt[gems[end]] == 1:
                unique += 1
            end += 1

        if unique == gem_type:
            if end - start - 1 < answer[1] - answer[0]:
                answer = (start, end - 1)

        gem_cnt[gems[start]] -= 1
        if gem_cnt[gems[start]] == 0:
            unique -= 1

    return [answer[0] + 1, answer[1] + 1]
