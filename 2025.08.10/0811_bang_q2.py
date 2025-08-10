r1 = [-1,0,0,1]
c1 = [0,-1,1,0]
r2 = [-1,-1,1,1]
c2 = [-1,1,-1,1]
rt = r1+r2
ct = c1+c2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max_fly = 0
    for r in range(N):
        for c in range(N):
            cnt = arr[r][c]
            for d in range(8):
                nr, nc = r + rt[d], c + ct[d]
                if 0<=nr<N and 0<=nc<N:
                    cnt += arr[nr][nc]

            if cnt > max_fly:
                max_fly = cnt
    print(f'#{tc} {max_fly}')
