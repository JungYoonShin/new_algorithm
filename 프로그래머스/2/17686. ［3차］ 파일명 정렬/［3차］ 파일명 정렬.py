def solution(files):
    answer = []
    
    #head, number, tail 3부분 
    #number는 최초로 숫자가 등장한 곳(최대 1-5글자의 숫자)
    for k, file in enumerate(files):
        number_appear = False
        number_start = 0
        number_end = 0
        for i, f in enumerate(file):
            if not number_appear and f.isdigit():
                number_start = i
                number_end = i
                number_appear = True
            elif number_appear and f.isdigit() and i - number_start < 5:
                number_end = i
            elif number_appear and not f.isdigit():
                break
            

        head = file[0:number_start]
        if head:
            head = head.lower()
        number = int(file[number_start:number_end+1])
        tail = file[number_end+1:]
        answer.append([file, head, number, k])
        
        print(head, number, tail)

    answer.sort(key=lambda x: (x[1], x[2], x[3]))
    answer = [x[0] for x in answer]
    return answer