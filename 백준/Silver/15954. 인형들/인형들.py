import math
n, k = map(int, input().split())
num = list(map(int, input().split()))

sum = [0] * n
sum[0] = num[0]

for i in range(1, n):
    sum[i] = sum[i-1] + num[i]
#k개 ~ n개 선택
result = []
for i in range(k, n+1):
    for j in range(n-i+1):
        #j부터 j+k-1까지(평균)
        if j==0:
            m = sum[j+i-1] / i
        else:
            m = (sum[j+i-1] - sum[j-1]) / i

        #분산 편차 구하기
        plus = 0
        for p in range(j, j+i):
            plus += (num[p]-m) ** 2
        plus = math.sqrt(plus / i)
        result.append(plus)

print(min(result))