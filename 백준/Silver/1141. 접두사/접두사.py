n = int(input())
words = [input().strip() for _ in range(n)]

words.sort(key=len, reverse=True)

selected = []

for w in words:
    ok = True
    for s in selected:
        if s.startswith(w):
            ok = False
            break
    if ok:
        selected.append(w)

print(len(selected))