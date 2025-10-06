def solution(numbers):
    answer = []
    
    def is_binary(num):
        mid = len(num) // 2
        if len(num) == 1:
            return True
        
        if num[mid] == '0':
            if '1' in num[0:mid] or '1' in num[mid+1:]:
                return False
                    
        return is_binary(num[0:mid]) and is_binary(num[mid+1:])
    
    for number in numbers:
        to_bin = bin(number)[2:]
        
        if len(to_bin) == 1:
            answer.append(int(to_bin))

        else:
            i = 1
            total = 1
            while True:
                i *= 2
                total += i
                if total >= len(to_bin):
                    to_be = total
                    break

            to_bin = '0' * (to_be - len(to_bin)) + to_bin
            answer.append(int(is_binary(to_bin)))
    
    return answer