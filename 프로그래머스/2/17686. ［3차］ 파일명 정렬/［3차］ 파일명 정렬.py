def solution(files):
    answer = []
    
    original_file = {}
    after_file = []
    
    for idx, file in enumerate(files):
        number_cnt, head_end = 0, -1
        for i, f in enumerate(file):
            if f.isdigit():
                if head_end == -1:
                    head_end = i-1
                number_end = i
                number_cnt += 1
            elif number_cnt != 0:
                    break
        
        head = file[0:head_end+1].lower()
        number = file[head_end+1:number_end+1]
        tail = file[number_end+1:]
        
        after_file.append([head, int(number), idx, file])
    
    after_file.sort(key = lambda x: (x[0], x[1], x[2]))
    return [x[3] for x in after_file]
