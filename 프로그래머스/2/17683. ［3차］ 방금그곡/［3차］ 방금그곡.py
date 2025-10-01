def solution(m, musicinfos):
    answer = ''
    
    possible = []
    len_m = len(m)
    m = m.replace("C#", "c").replace("D#", "d").replace("B#", "C").replace("E#", 'F') \
             .replace("F#", "f").replace("G#", "g").replace("A#", "a")
    i = 0
    for musicinfo in musicinfos:
        start, end, name, music = musicinfo.split(",")
        music_split = music.replace("C#", "c").replace("D#", "d").replace("B#", "C").replace("E#", 'F') \
             .replace("F#", "f").replace("G#", "g").replace("A#", "a")

            
        sm, ss = map(int, start.split(":"))
        em, es = map(int, end.split(":"))
        
        total_time = (em * 60 + es) - (sm * 60 + ss)
        
        music_len = len(music_split)
        play = music_split * (total_time // music_len) + music_split[0:total_time % music_len]
        print(play)
                
        if m in play:
            possible.append([total_time, i, name])
        i+= 1
    
    possible.sort(key = lambda x : (-x[0], x[1]))
    if not possible:
        return "(None)"
    
    return possible[0][2]