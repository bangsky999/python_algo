### 5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크 ### 
'''
a = [[4, 14], [8, 18], [17, 20], [20, 23], [23, 24]]
2차원의 list를 a[1]의 크기순으로 정렬하고 싶다?
a.sort(key = lambda x: x[1])
'''
import sys; sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 5
    schedule = []
    for _ in range(N):
        start, end = list(map(int, input().split())) # [14,23]
        schedule.append([start, end])

    time_table = [0]*24 # 간격으로 세기
    schedule.sort(key=lambda x : x[1]) # 정렬 중요 !!!!
    # print(schedule) # [[4, 14], [8, 18], [17, 20], [20, 23], [23, 24]]
    cnt = 0
    
    # print(time_table)
    for i in schedule: # i = [4,14] , time_table의 4~ 13번까지 0인지 확인 후 
        val = 1 # 스케쥴 체크
        for j in range(i[0], i[1]): # 4 ~ 13
            if time_table[j] != 0: # 이미 스케쥴이 차있으면 나가라
                val = 0
                break
            # 스케쥴이 안차 있다면 
        if val == 1:
            cnt += 1
            for k in range(i[0], i[1]):
                time_table[k] = 1



    print(f'#{tc} {cnt}')