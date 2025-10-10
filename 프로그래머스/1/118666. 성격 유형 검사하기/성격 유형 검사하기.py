from collections import defaultdict
def solution(survey, choices):
    answer = ''
    
    score = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3} #choices에 따른 각 점수
    
    result = defaultdict(int)
    
    for idx, s in enumerate(survey):
        left, right = s[0], s[1]
        
        if choices[idx] < 4:
            result[left] += score[choices[idx]]
        else:
            result[right] += score[choices[idx]]
    print(result)
    
    if result["R"] >= result["T"]: answer += 'R'
    else: answer += 'T'
    if result['C'] >= result['F']: answer += 'C' 
    else: answer += 'F'
    if result['J'] >= result['M']: answer += 'J'
    else: answer += 'M'
    if result['A'] >= result['N']: answer += 'A'
    else: answer += 'N'
    return answer