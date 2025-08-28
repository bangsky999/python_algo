### 스위치 켜고 끄기 ###

N = int(input()) # 스위치의 개수
switch = list(map(int, input().split())) # 입력받은 스위치 [0,1,0,1,0,0,0,1]
stu_num = int(input())
for stu in range(stu_num): # 2명 // 1 3 // 2 3
    gender, get_num = map(int, input().split()) # 1 3
    if gender == 1: # 남학생이면
        for i in range(1, N+1): # i의 값 : 1~8
            if i % get_num == 0:
                switch[i-1] = 1-switch[i-1]
    else: # 여학생이면
        for i in range(N): # i의 값은 0~(N-1)
            if 0 <= (get_num-1)-i and (get_num-1)+i <= N-1 and switch[(get_num-1)-i] == switch[(get_num-1)+i]: 
                if (get_num-1)-i == (get_num-1)+i:
                    switch[(get_num-1)-i] = 1 - switch[(get_num-1)-i]
                else:
                    switch[(get_num-1)-i], switch[(get_num-1)+i] = 1 - switch[(get_num-1)-i], 1 - switch[(get_num-1)+i]
            else:
                break
if N <= 20:
    print(*switch)
elif 20 < N <= 40:
    lst1 = switch[0:20]
    lst2 = switch[20:]
    print(*lst1)
    print(*lst2)
elif 40 < N <= 60:
    lst1 = switch[0:20]
    lst2 = switch[20:40]
    lst3 = switch[40:]
    print(*lst1)
    print(*lst2)
    print(*lst3)
elif 60 < N <= 80:
    lst1 = switch[0:20]
    lst2 = switch[20:40]
    lst3 = switch[40:60]
    lst4 = switch[60:]
    print(*lst1)
    print(*lst2)
    print(*lst3)
    print(*lst4)
elif 80 < N <= 100:
    lst1 = switch[0:20]
    lst2 = switch[20:40]
    lst3 = switch[40:60]
    lst4 = switch[60:80]
    lst5 = switch[80:]
    print(*lst1)
    print(*lst2)
    print(*lst3)
    print(*lst4)
    print(*lst5)

