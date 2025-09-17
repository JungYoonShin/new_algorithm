def solution(lottos, win_nums):
    answer = []
    
    correct = 0
    unknown = 0
    uncorrect = 0
    
    for lotto in lottos:
        #일단 완전 맞는 번호 개수구함
        if lotto in win_nums:
            correct += 1
        elif lotto == 0:
            unknown += 1
        else:
            uncorrect += 1
        
    max_correct = correct+unknown
    min_correct = len(lottos) - (unknown + uncorrect)
    
    if max_correct < 2:
        answer.append(6)
    else:
        answer.append(7-max_correct)
    
    if min_correct < 2:
        answer.append(6)
    else:
        answer.append(7-min_correct)
    
    print(max_correct, min_correct)
    
    return answer