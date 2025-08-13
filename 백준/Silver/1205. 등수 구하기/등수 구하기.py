import sys, copy
input = sys.stdin.readline

n, new_score, p = map(int, input().split())
score = list(map(int, input().split())) if n > 0 else []
score.sort(reverse=True)


if len(score) == 0:
    print(1)
    exit()


elif len(score) == p:
    if score[-1] >= new_score:
        print(-1)
        exit()

rank = 1
for i in range(n):
    if score[i] > new_score:
        rank += 1
    else:
        break
print(rank)
