from heapq import heappush, heappop

def solution(n, k, enemy):
    heap = []

    for idx, e in enumerate(enemy):
        heappush(heap, e)

        if len(heap) > k:
            n -= heappop(heap)
            if n < 0:
                return idx

    return len(enemy)