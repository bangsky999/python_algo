N = int(input())

new_num = ''
cnt = 0

if cnt == 0:
    if N < 10:
        total = 0 + N # 01
        new_num = str(N) + str(total)[-1] # 11
        cnt += 1
    elif N >= 10:
        total = int(str(N)[0]) + int(str(N)[1])
        new_num = str(N)[1] + str(total)[-1]
        cnt += 1
if cnt > 0:
    while N != int(new_num):
        if int(new_num) < 10:
            total = 0 + int(new_num)
            new_num = str(new_num) + str(total)[-1]
            cnt += 1
        elif int(new_num) >= 10:
            total = int(str(new_num)[0]) + int(str(new_num)[1]) 
            new_num = str(new_num)[1] + str(total)[-1]
            cnt += 1

print(cnt)