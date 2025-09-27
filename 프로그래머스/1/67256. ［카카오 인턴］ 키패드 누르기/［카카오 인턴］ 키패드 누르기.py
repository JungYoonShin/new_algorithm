def solution(numbers, hand):
    answer = ''
    
    l_thumb = [3, 0]
    r_thumb = [3, 2]
    
    number_graph = {1: [0, 0], 2:[0,1], 3:[0, 2], 4: [1, 0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2, 2], 0:[3, 1]}
    
    hand = hand[0].upper()
    
    for number in numbers:
        
        
        if number in [1, 4, 7]:
            l_thumb = number_graph[number]
            answer += 'L'
        elif number in [3, 6, 9]:
            r_thumb = number_graph[number]
            answer += 'R'
        else:
            number_x, number_y = number_graph[number]
            
            
            distance_l = abs(l_thumb[0] - number_x) + abs(l_thumb[1] - number_y)
            distance_r = abs(r_thumb[0] - number_x) + abs(r_thumb[1] - number_y)
            if distance_l == distance_r:
                answer += hand
                if hand == 'R':
                    r_thumb = [number_x, number_y]
                else:
                    l_thumb = [number_x, number_y]
            elif distance_l < distance_r:
                answer += 'L'
                l_thumb = [number_x, number_y]
            else:
                answer += 'R'
                r_thumb = [number_x, number_y]
                
    return answer