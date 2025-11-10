from collections import defaultdict

n = int(input())
order = defaultdict(list)
all_alphabet = []

for _ in range(n):
    alphabet = input()
    all_alphabet.append(alphabet)
    length = len(alphabet)
    for i in range(length - 1, -1, -1):
        order[alphabet[i]].append(10 ** (length - i - 1))

new_order = []
for a in order.keys():
    total_weight = sum(order[a])
    new_order.append((a, total_weight))

new_order.sort(key=lambda x: -x[1])

alphabet_num = defaultdict(lambda: -1)
start = 9

for value in new_order:
    alphabet_num[value[0]] = start
    start -= 1

answer = 0
for a in all_alphabet:
    num = ''
    for x in a:
        num += str(alphabet_num[x])
    answer += int(num)

print(answer)