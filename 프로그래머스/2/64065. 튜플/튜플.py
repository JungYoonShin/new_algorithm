from collections import Counter
import re
def solution(s):
    answer = []
    
    nums = re.findall("\d+", s)
    return [int(x[0]) for x in sorted(Counter(nums).items(), key = lambda x : x[1], reverse = True)]
