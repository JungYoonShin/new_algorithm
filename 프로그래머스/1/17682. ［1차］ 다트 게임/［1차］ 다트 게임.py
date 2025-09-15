def solution(dartResult):
    score = [0]
    area_score = {'S': 1, 'D': 2, 'T': 3}
    
    s = ''
    for d in dartResult:
        if d.isdigit():
            s += d
        
        elif d in area_score:  # 보너스 S/D/T
            n = int(s)
            score.append(n ** area_score[d])
            s = ''
        
        elif d == '*':
            if score:
                score[-1] *= 2
                score[-2] *= 2
        elif d == '#':
            if score:
                score[-1] *= -1
    
    return sum(score)
