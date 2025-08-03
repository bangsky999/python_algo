N = int(input())
for i in range(1, N+1):
    M = int(input())
    value = M
    cnt_2 = 0
    cnt_3 = 0
    cnt_5 = 0
    cnt_7 = 0
    cnt_11 = 0
    val = True
    while val == True:
        # 모든 조건을 if로 처리하면, 모든 조건을 순서대로 처리
        # elif는 위 조건이 만족되면 다시 위에서부터 시작됨
        if value % 2 == 0:
            value = value // 2
            cnt_2 += 1
        elif value % 3 == 0:
            value = value // 3
            cnt_3 += 1
        elif value % 5 == 0:
            value = value // 5
            cnt_5 += 1
        elif value % 7 == 0:
            value = value // 7
            cnt_7 += 1
        elif value % 11 == 0:
            value = value // 11
            cnt_11 += 1
        else:
            print(f'#{i} {cnt_2} {cnt_3} {cnt_5} {cnt_7} {cnt_11}')
            val = False