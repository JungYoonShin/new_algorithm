def solution(play_time, adv_time, logs):
    answer = -1e9
    
    def time_to_sec(time):
        hour, minute, sec = map(int, time.split(":"))
        return hour * 60 * 60 + minute * 60 + sec
    
    play_time_sec = time_to_sec(play_time)
    adv_time_sec = time_to_sec(adv_time)
    
    watch = [0] * (play_time_sec + 1)
    
    for log in logs:
        start, end = log.split("-")
        watch[time_to_sec(start)] += 1
        watch[time_to_sec(end)] -= 1
    
    for i in range(1, len(watch)):
        watch[i] += watch[i-1]
        
    for i in range(1, len(watch)):
        watch[i] += watch[i-1]
    
    result = 0
    for i in range(adv_time_sec, play_time_sec+1):
        current = watch[i] - watch[i - adv_time_sec]  #i가 광고 끝나는 지점
        if current > answer:
            answer = current
            result = i - adv_time_sec + 1
            
    h = result // 3600
    m = (result % 3600) // 60
    s = (result % 3600) % 60 
    
    if result == 1:
        return "00:00:00"
    return f"{h:02}:{m:02}:{s:02}"
    