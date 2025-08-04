from bisect import bisect_left
def solution(A, B):
    answer = 0
    
    A.sort()
    B.sort()
    
    a, b = 0, 0
    
    while a < len(A) and b < len(B):
        if B[b] > A[a]:
            answer += 1
            a += 1
        b += 1
    return answer