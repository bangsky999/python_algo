# 각자리수 곱하기
A, B = map(str, input().split())

sum = 0
a = len(A) # 3
b = len(B) # 2
for i in range(a):
    for j in range(b):
        sum += int(A[i])*int(B[j])

print(sum)

