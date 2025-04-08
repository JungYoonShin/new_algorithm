import sys
import heapq

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    m = int(input())
    nums = []

    while len(nums) < m:
        nums += list(map(int, input().split()))

    left = []  # 최대 힙 (중간 이하)
    right = []  # 최소 힙 (중간 초과)
    result = []

    for i in range(m):
        num = nums[i]

        heapq.heappush(left, -num)

        if len(left) == len(right):
            heapq.heappush(left, -num)
            # max_heap과 min_heap의 크기가 다르면 이전에 최대 힙에 넣은 것이기 때문에
            # 개수를 맞춰주기 위해 최소 힙에 값을 넣는다.
        else:
            heapq.heappush(right, num)

        # 대소 조건 비교하기
        # min_heap의 root 값이 max_heap의 root 값보다 작다면 두 수를 바꿔준다.
        if right and -left[0] > right[0]:
            heapq.heappush(right, -heapq.heappop(left))
            heapq.heappush(left, -heapq.heappop(right))

        if i % 2 == 0:
            result.append(-left[0])

    # 출력 형식
    print(len(result))
    for i in range(len(result)):
        print(result[i], end=' ')
        if (i + 1) % 10 == 0:
            print()
    if len(result) % 10 != 0:
        print()
