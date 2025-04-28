import copy
def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        new_array = copy.deepcopy(array)
        new_array = new_array[i-1:j]
        new_array.sort()
        answer.append(new_array[k-1])
    
    return answer