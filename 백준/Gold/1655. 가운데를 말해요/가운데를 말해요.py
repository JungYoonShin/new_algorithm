import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
max_heap = []  #중앙값보다 작은 값
min_heap = []  #중앙값보다 큰 값

for _ in range(n):
    num = int(input())
    if len(max_heap) == len(min_heap):
        heappush(max_heap, -num)
    else:
        heappush(min_heap, num)

    #두 힙간의 root 대소 비교하기
    if min_heap and -max_heap[0] > min_heap[0]:
        temp_max = heappop(max_heap)
        temp_min = heappop(min_heap)
        heappush(max_heap, -temp_min)
        heappush(min_heap, -temp_max)

    print(-max_heap[0])