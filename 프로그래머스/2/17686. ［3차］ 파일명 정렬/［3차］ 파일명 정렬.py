def solution(files):
    answer = []
    
    original_file = {}
    after_file = []
    
    for idx, file in enumerate(files):
        head_end = -1
        number_start = -1
        number_end = -1

        for i, ch in enumerate(file):
            if ch.isdigit():
                if number_start == -1:
                    number_start = i
                    head_end = i - 1
                number_end = i
            elif number_start != -1:
                break
        
        head = file[0:head_end+1].lower()
        number = file[head_end+1:number_end+1]
        tail = file[number_end+1:]
        after_file.append([head, int(number), idx, file])
    
    after_file.sort(key = lambda x: (x[0], x[1], x[2]))
    print(after_file)
    return [x[3] for x in after_file]