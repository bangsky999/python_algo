import sys; sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[1]*i for i in range(1,N+1)]

    for r in range(2,N):
         for c in range(1,r): # 중요 포인트 
            arr[r][c] = arr[r-1][c-1] + arr[r-1][c]

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])
