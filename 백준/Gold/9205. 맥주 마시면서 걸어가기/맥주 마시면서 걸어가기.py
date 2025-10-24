from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    x, y = map(int, input().split())
    store = [list(map(int, input().split())) for _ in range(n)]
    festival_x, festival_y = map(int, input().split())

    q = deque([(x, y)])
    visited = [False] * n
    answer = False
    while q:
        a, b = q.popleft()

        if abs(festival_x - a) + abs(festival_y - b) <= 1000:
            answer = True
            break

        for i in range(n):
            store_x, store_y = store[i]
            if not visited[i]:
                if abs(store_x - a) + abs(store_y - b) <= 1000:
                    visited[i] = True
                    q.append((store_x, store_y))


    if answer == True:
        print("happy")
    else:
        print("sad")


