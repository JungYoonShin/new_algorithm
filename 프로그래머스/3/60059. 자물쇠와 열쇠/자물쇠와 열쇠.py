def solution(key, lock):
    answer = True
    
    n = len(lock)
    m = len(key)
    
    graph = [[0 for _ in range(n*3)] for _ in range(n*3)]
    
    for i in range(n):
        for j in range(n):
            graph[i+n][j+n] = lock[i][j]
    
    def rotate(key):
        return list(map(list, zip(*key[::-1])))
        
    
    for i in range(2*n+1):
        for j in range(2*n+1):
            for k in range(4):
                key = rotate(key)
                for p in range(m):
                    for q in range(m):
                        graph[i+p][j+q] += key[p][q]
                
                cnt = 0
                for p in range(n):
                    for q in range(n):
                        if graph[p+n][q+n] == 1:
                            cnt += 1
                # print(cnt)
                # print(i, j)
                # print(*key, sep="\n")
                # print(*graph, sep="\n")
                # print()
                #열쇠로 자물쇠를 열 수 있는 경우
                if cnt == n*n:
                    return True
                
                for p in range(m):
                    for q in range(m):
                        graph[i+p][j+q] -= key[p][q]
                
    return False