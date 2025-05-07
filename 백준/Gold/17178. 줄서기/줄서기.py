import sys
input=sys.stdin.readline

n = int(input())
ticket = []
for _ in range(n):
    ticket.extend(input().split())

sorted_tickets = sorted(ticket, key=lambda x: (x.split('-')[0], int(x.split('-')[1])))
order = {}
for i, j in enumerate(sorted_tickets):
    order[j] = i
stack = []
waiting = []
for t in ticket:
    while waiting and order[waiting[-1]] == len(stack):
        stack.append(waiting.pop())

    if order[t] == len(stack):
        stack.append(t)
    else:
        waiting.append(t)

while waiting:
    stack.append(waiting.pop())

if sorted_tickets != stack:
    print("BAD")
else:
    print("GOOD")

