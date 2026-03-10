n = int(input())
alphabet = [input() for _ in range(n)]

alphabet.sort(key=len, reverse= True)

result = []

for a in alphabet:
    flag = False
    for group in result:
        if group.startswith(a):
            flag = True
            break
    if not flag:
        result.append(a)

    result.sort(key=lambda x: -len(x))

print(len(result))