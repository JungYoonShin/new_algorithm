answer = -1
def solution(k, dungeons):
    cnt = len(dungeons)
    
    visited = [False] * len(dungeons)
    
    def explore(get, left):
        global answer
        for v, dun in enumerate(dungeons):
            if not visited[v] and left >= dun[0]:
                visited[v] = True
                get.append(v)
                left -= dun[1]
                explore(get, left)
                visited[v] = False
                get.pop()
                left += dun[1]
                
        if answer < len(get):
            answer = len(get)
            return
            
    explore([], k)
    print(answer)
    
    return answer