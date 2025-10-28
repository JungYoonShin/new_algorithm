def solution(m, n, startX, startY, balls):
    answer = []
    
    for targetX, targetY in balls:
        #위쪽 벽 반사
        up = (startX - targetX) ** 2 + ((2*n - targetY) - startY) ** 2
        
        down = (startX - targetX) ** 2 + (startY + targetY) ** 2
        
        left = (startX + targetX) ** 2 + (startY - targetY) ** 2
        
        right = ((2*m - targetX) - startX) ** 2 + (targetY - startY) ** 2
        
        result = [up, down, left, right]
        
        if startX == targetX and startY > targetY:
            result.remove(down)
        
        if startX == targetX and startY < targetY:
            result.remove(up)
        
        if startY == targetY and startX > targetX:
            result.remove(left)
        
        if startY == targetY and startX < targetX:
            result.remove(right)
        
        answer.append(min(result))
            

    return answer