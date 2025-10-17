def solution(dirs):
    answer = 0
    
    direction = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    x, y = 5, 5
    visited = set()
    
    for dir in dirs:
        move = direction[dir]
        nx = x + move[0]
        ny = y + move[1]
        
        if 0<=nx<=10 and 0<=ny<=10:
            if ((x, y), (nx, ny)) not in visited and ((nx, ny), (x, y)) not in visited:
                visited.add(((x, y), (nx, ny)))
                visited.add(((nx, ny), (x, y)))
                answer += 1
            x, y = nx, ny
    
    return answer