### 나는 달팽이한테 졌다 ### 
# import sys
# sys.stdin = open("input.txt")

# 방향 순서는 우, 아래, 좌, 위
dr = [0,1,0,-1]
dc = [1,0,-1,0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    
    # r은 세로, c은 가로, d는 방향
    r, c, d = 0, 0, 0
    # 시작값
    cnt = 1
    arr[r][c] = cnt

    while cnt < N*N:
        nr, nc = r + dr[d], c + dc[d]
        if 0<=nr<N and 0<=nc<N and arr[nr][nc] == 0:
            cnt += 1
            arr[nr][nc] = cnt
            r, c = nr, nc
        else:
            d = (d+1)%4

    print(f'#{tc}')            
    for row in arr:
        print(' '.join(map(str, row)))
        
            
                
                