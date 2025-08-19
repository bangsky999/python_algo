N = 10
score_list = [int(input()) for _ in range(N)]

sum1 = 0 # 100직전의 sum값
sum2 = 0 # 100직후의 sum값
for i in range(10):
    sum1 += score_list[i]
    sum2 += score_list[i]
    if sum2 > 100:
        sum1 -= score_list[i]
        break
if (100 - sum1) < (sum2 - 100):
    print(sum1)
else:
    print(sum2)
