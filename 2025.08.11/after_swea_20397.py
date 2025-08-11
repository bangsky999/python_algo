import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    
    for _ in range(1,M+1):
        i, j = map(int, input().split())
        for l in range(1,j+1):
            if 0<=arr[i-1-l]<N and 0<=arr[i-1+l]<N:
                if arr[i-1-l] == arr[i-1+l] and arr[i-1-l] == 0 and arr[i-1+l] == 0:
                    arr[i-1-l], arr[i-1+l] = 1, 1
                
                elif arr[i-1-l] == arr[i-1+l] and arr[i-1-l] == 1 and arr[i-1+l] == 1:
                    arr[i-1-l], arr[i-1+l] = 0, 0
            else: 
                break
    print(f'#{tc}', end = ' ')
    print(' '.join(map(str, arr)))
    