import sys

input = sys.stdin.readline

n = int(input())
budget = list(map(int, input().split()))
full_budget = int(input())

start = 0
end = max(budget)

def binary_search(start, end):
  result = 0
  while start <= end:
    total = 0
    mid = (start+end)//2
    for money in budget:
      if money > mid:
        total += mid
      else:
        total += money
    if total > full_budget:
      end = mid - 1
    else:
      result = mid
      start = mid + 1     
  return result

print(binary_search(start, end))