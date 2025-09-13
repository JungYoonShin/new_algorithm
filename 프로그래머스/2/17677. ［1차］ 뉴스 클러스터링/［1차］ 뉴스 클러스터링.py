from collections import defaultdict
def solution(str1, str2):
    answer = 0

    str1 = str1.lower()
    str2 = str2.lower()
    
    s1_cnt = defaultdict(int)
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            s = str1[i] + str1[i+1]
            s1_cnt[s] += 1
            
    s2_cnt = defaultdict(int)
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            s = str2[i] + str2[i+1]
            s2_cnt[s] += 1
    
    # 교집합 크기
    inter = 0
    for s in s1_cnt:
        if s in s2_cnt:
            inter += min(s1_cnt[s], s2_cnt[s])
    
    # 합집합 크기
    union = 0
    keys = set(s1_cnt.keys()) | set(s2_cnt.keys())
    for s in keys:
        union += max(s1_cnt[s], s2_cnt[s])
    
    if inter == 0 and union == 0:
        answer = 65536
    
    else:
        answer = int((inter/union) * 65536)
    
    return answer