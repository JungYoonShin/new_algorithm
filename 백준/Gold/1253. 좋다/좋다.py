# N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.
# N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.
# 수의 위치가 다르면 값이 같아도 다른 수이다.

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

nums.sort()
answer = 0

for i in range(n):
    target = nums[i]
    temp = nums[:i] + nums[i + 1:]
    start = 0
    end = len(temp)-1

    while start < end:
        sum = temp[start] + temp[end]
        if sum == target:
            answer+=1
            break
        elif sum > target:
            end-=1
        else:
            start +=1
print(answer)