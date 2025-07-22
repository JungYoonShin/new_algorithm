import sys

input = sys.stdin.readline

# 길이가 N인 수열이 주어질 때, 수열에서 연속한 1개 이상의 수를 뽑았을 때 같은 수가 여러 번 등장하지 않는 경우의 수를 구하는 프로그램을 작성하여라.

n = int(input())
nums = list(map(int, input().split()))
visited = [False] * 100001

start, end = 0, 0
result = 0
while start < n:
    while end < n and not visited[nums[end]]:
        visited[nums[end]] = True
        end += 1

    result += end - start
    visited[nums[start]] = 0
    start += 1
print(result)