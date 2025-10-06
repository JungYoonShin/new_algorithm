def solution(files):
    answer = []
    
    new = []
    for file in files:
        head, num, tail = '', '', ''
        is_num = False
        for i in range(len(file)):
            if file[i].isdigit():
                num += file[i]
                is_num = True
            elif not is_num:
                head += file[i]
            else:
                tail += file[i:]
                break
                
        new.append((head, num, tail))
        
    new.sort(key=lambda x: (x[0].upper(), int(x[1])))
    return [''.join(t) for t in new]