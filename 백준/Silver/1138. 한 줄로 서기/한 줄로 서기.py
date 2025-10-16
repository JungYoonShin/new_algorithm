n = int(input())
info = list(map(int, input().split()))

result = [0] * n

for person in range(n):
    taller_left = info[person]
    count = 0

    for i in range(n):
        if result[i] == 0: #나보다 큰 사람
            if count == taller_left:
                result[i] = person + 1
                break
            count += 1

print(*result)
