n = int(input())
alphabet = [input() for _ in range(n)]
alphabet.sort(key = lambda x: (-len(x)))
# print(alphabet)


result = [[]]

for a in alphabet:
    for group in result:
        flag = True
        for g in group:
            if g == a:
                flag = False
                break

            if g.startswith(a) or a.startswith(g):
                flag = False
                break

        #해당 그룹에 넣을 수 있다
        if flag:
            group.append(a)
            break
    else:
        result.append([a])
    result.sort(key = lambda x: -len(x))

print(len(result[0]))