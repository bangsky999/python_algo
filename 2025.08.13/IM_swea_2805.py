### 농작물아 자라라 ###
import sys; sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    cnt = 0 # 농작물 총 가치
    mid = N//2 # 중간값
    
    for r in range(mid+1):
        lst = arr[r][mid-r:mid+r+1]
        cnt += sum(lst)

    for r in range(mid+1,N):
        lst = arr[r][mid-(N-1-r):mid+(N-1-r)+1] # 폭의 절반 길이만큼
        cnt += sum(lst)

    print(f'#{tc} {cnt}')
