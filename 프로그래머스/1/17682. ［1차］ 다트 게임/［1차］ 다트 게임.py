def solution(dartResult):
    answer = 0
    
    dart = []
    result = ''
    
    dartResult = dartResult.replace('10', 'N')

    for i in range(len(dartResult)-1):
        result += dartResult[i]
        if dartResult[i+1].isdigit() or dartResult[i+1] == 'N':
            dart.append(result)
            result = ''
    dart.append(result + dartResult[i+1:])
    
    score = [0]
    area_score = {'S': 1, 'D': 2, 'T': 3}
    
    i=1
    for d in dart:
        if len(d) == 3:
            n, area, award = d
            if n == 'N':
                n = 10
            n = int(n)
            if award == '*':
                score[i-1] = score[i-1] * 2
                score.append((n ** area_score[area]) * 2)

            else:
                score.append(-1 * (n ** area_score[area]))
        else:
            n, area = d
            if n == 'N':
                n = 10
            n = int(n)
            score.append(n ** area_score[area])
                
        i+=1
    

    return sum(score)