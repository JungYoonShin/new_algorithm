def solution(book_time):
    answer = 0
    book_time.sort()
    status = []
    
    for time in book_time:
        start, end = time
        end_hour, end_minute = map(int, end.split(":"))
        end_total = end_hour * 60 + end_minute + 10
        start_hour, start_minute = map(int, start.split(":"))
        start_total = start_hour * 60 + start_minute
        
        if not status:
            status.append(end_total)
        
        else:
            for i, s in enumerate(status):
                if s <= start_total:
                    status[i] = end_total
                    break
            else:
                status.append(end_total)
                    
    return len(status)