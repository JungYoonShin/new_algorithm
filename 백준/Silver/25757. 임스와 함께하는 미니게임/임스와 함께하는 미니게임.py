import sys

input = sys.stdin.readline

done = []

game = {'Y':2, "F":3, "O": 4}

n, type = input().split()
n = int(n)

people = []
time = game[type]-1

for _ in range(n):
    people.append(input())

people = list(set(people))

print(len(people) // time)