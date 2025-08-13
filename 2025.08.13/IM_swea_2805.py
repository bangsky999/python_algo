### 농작물아 자라라 ###
import sys; sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    cnt = 0 # 농작물 총 가치
    mid = N//2 # 중간값
    
    for r in range(mid+1):
        for c in range(0,mid+1):
            lst = arr[r][mid-c:mid+c+1]
            for i in lst:
                cnt += i
    ######### print
    for r in range(mid+1,N):
        for c in range(mid-1, -1, -1):
            lst =  arr[r][mid-c:mid+c+1]
            for i in lst:
                cnt += i

    print(f'#{tc} {cnt}')
