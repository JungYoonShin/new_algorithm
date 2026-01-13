n = int(input()) #시험장 개수
student = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0

for s in student:
    remain = s - b
    answer += 1

    if remain > 0:
        if remain % c == 0:
            answer += (remain // c)
        else:
            answer += (remain // c + 1)

print(answer)