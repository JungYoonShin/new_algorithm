def solution(numbers):
    result = []
    
    def check(nodes):
        if not nodes:
            return True
        
        mid = len(nodes) // 2
        if nodes[mid] == '0':
            if '1' in nodes:
                return False
            return True
            
        return check(nodes[:mid]) and check(nodes[mid+1:])
        
    
    for number in numbers:
        number = bin(number)[2:]
        
        if len(number) % 2 == 0:
            number = '0' + number
        
        n = len(number)
        
        #포화이진트리 높이 구하기
        answer = 1
        height = 1
        while answer < n:
            answer += height
            height *= 2
        
        #부족한만큼 앞을 0으로 채우기
        while True:
            if len(number) == answer:
                break
            number = '0' + number
        
        result.append(int(check(number)))
            
    return result