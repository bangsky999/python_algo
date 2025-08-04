# 1번 답변

for t in range(1, 11): # 무조건 10번을 돌림
    N = int(input()) # 건물 갯수
    arr = list(map(int, input().split())) # 건물 높이의 배열
    tall_num = 0 # 조망권 세대수의 합
    for i in range(N-4):
        big_num = 0
        sec_num = 0
        for j in arr[i: i+5]:
            if j > big_num: # 최대, 2nd num 찾기 x
                sec_num = big_num
                big_num = j
            elif big_num >= j > sec_num: # sec값이 big과 같을 수가 없어져서 예외 발생
                sec_num = j
    
        if arr[i+2] == big_num:
            tall_num += (big_num - sec_num)

    print(f'#{t} {tall_num}')




# 2번 답변

for t in range(1, 11): # 무조건 10번을 돌림
    N = int(input()) # 건물 갯수
    arr = list(map(int, input().split())) # 건물 높이의 배열
    tall_num = 0 # 조망권 세대수의 합
    for i in range(N-4):
        mid_h = arr[i+2]
        others = arr[i:i+2]+arr[i+3:i+5]
        other_max = max(others)
        if mid_h > other_max:
            tall_num += (mid_h - other_max)   
    print(f'#{t} {tall_num}')




# 3번 답변 

for t in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    tall_num = 0
    for i in range(2, N-2):

        mid_h = arr[i]
        others_h = max(arr[i-2:i]+arr[i+1:i+3])

        if mid_h > others_h:
            tall_num += (mid_h - others_h)

    print(f'#{t} {tall_num}')



























