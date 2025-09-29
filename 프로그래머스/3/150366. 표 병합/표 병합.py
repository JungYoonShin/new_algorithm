def solution(commands):
    answer = []
    
    parent = [[0 for _ in range(51)] for _ in range(51)]
    
    value = [["" for _ in range(51)] for _ in range(51)]
    
    #초기 값은 스스로를 가리킴
    for i in range(1, 51):
        for j in range(1, 51):
            parent[i][j] = [i, j]
    
    def getParent(x, y):
        if parent[x][y] != [x, y]:
            parent[x][y] = getParent(parent[x][y][0], parent[x][y][1])
        return parent[x][y]


    def union(r1, c1, r2, c2):
        pr1, pc1 = getParent(r1, c1)
        pr2, pc2 = getParent(r2, c2)

        if [pr1, pc1] == [pr2, pc2]:
            return

        # 대표값 정하기
        merged_value = value[pr1][pc1] if value[pr1][pc1] != "" else value[pr2][pc2]

        # 그룹 전체 parent 갱신
        for i in range(1, 51):
            for j in range(1, 51):
                if getParent(i, j) == [pr2, pc2]:
                    parent[i][j] = [pr1, pc1]

        value[pr1][pc1] = merged_value

    
    for command in commands:    
        # print(value[0], value[1], value[2])
        query = command.split(" ")
        n = len(query)
        if query[0] == 'UPDATE':
            # UPDATE value1 value2
            if n == 3:
                v1, v2 = query[1:]
                for i in range(1, 51):
                    for j in range(1, 51):
                        p = getParent(i, j)
                        if value[p[0]][p[1]] == v1:
                            value[p[0]][p[1]] = v2
            
            # UPDATE r c value
            else:
                r, c = map(int, query[1:3])
                v = query[3]
                p = getParent(r, c)
                value[p[0]][p[1]] = v
        
        elif query[0] == 'MERGE':
            r1, c1, r2, c2 = map(int, query[1:])
            union(r1, c1, r2, c2)
            
        elif query[0] == 'UNMERGE':
            r, c = map(int, query[1:])
            p = getParent(r, c)
            remain_value = value[p[0]][p[1]]
            
            group = []
            for i in range(1, 51):
                for j in range(1, 51):
                    if getParent(i, j) == [p[0], p[1]]:
                        group.append([i, j])
                
            for x, y in group:
                parent[x][y] = [x, y]      
                value[x][y] = ""
            
            value[r][c] = remain_value         
        
        else:
            r, c = map(int, query[1:])
            p = getParent(r, c)
            if value[p[0]][p[1]] == "":
                answer.append("EMPTY")
            else:
                answer.append(value[p[0]][p[1]])
        # print(value[0], value[1], value[2])
    return answer