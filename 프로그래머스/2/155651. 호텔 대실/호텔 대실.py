def solution(book_time):
    answer = 0
    
    rooms = []
    
    book_time.sort()

    
    for b in book_time:
        s_hour, s_minute = map(int, b[0].split(":"))
        e_hour, e_minute = map(int, b[1].split(":"))
        
        if len(rooms) == 0:
            rooms.append([e_hour * 60 + e_minute + 10])
        else:
            new = False
            for i in range(len(rooms)):
                if rooms[i][-1] <= s_hour * 60 + s_minute:
                    new = True
                    rooms[i].append(e_hour * 60 + e_minute + 10)
                    break
            if not new:
                rooms.append([e_hour * 60 + e_minute + 10])
                
    print(rooms)
    
    return len(rooms)