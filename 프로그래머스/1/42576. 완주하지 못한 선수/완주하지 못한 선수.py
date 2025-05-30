from collections import defaultdict
def solution(participant, completion):
    answer = ''
    
    participant_dict = defaultdict(int)
    for p in participant:
        participant_dict[p] += 1
    
    for c in completion:
        participant_dict[c] -= 1
        if participant_dict[c] == 0:
            del participant_dict[c]
    a = participant_dict.keys()
    return list(a)[0]