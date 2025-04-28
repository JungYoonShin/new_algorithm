def solution(nums):
    answer = 0
    
    n = len(nums) // 2
    nums = list(set(nums))

    
    if n<= len(nums):
        return n
    else:
        return len(nums)
        