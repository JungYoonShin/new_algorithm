import sys
import heapq

input = sys.stdin.readline

#마시는 맥주 N개의 선호도 합이 M이상이 되게 하려 합니다. + 매일 다른 종류 맥주 먹어야 함
#간 레벨의 최솟값

n, m, k = map(int, input().split())
beer = [list(map(int, input().split())) for _ in range(k)]
beer.sort(key=lambda x:x[1])

prefer_list = []
prefer_sum = 0
answer = -1
for prefer, level in beer:
    heapq.heappush(prefer_list, prefer)
    prefer_sum += prefer

    if len(prefer_list) > n:
        a = heapq.heappop(prefer_list)
        prefer_sum -= a

    if len(prefer_list) == n and prefer_sum >= m:
        answer = level
        break

print(answer)