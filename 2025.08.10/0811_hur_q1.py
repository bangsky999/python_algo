import sys
sys.stdin = open("input.txt")

# +방향 방향벡터
r1 = [-1,0,0,1]
c1 = [0,-1,1,0]

# x방향 방향벡터
r2 = [-1,-1,1,1]
c2 = [-1,1,-1,1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max_fly = 0
    for r in range(N):
        for c in range(N):
            cnt = arr[r][c]
    # + 검사 
            for d in range(4):
                for m in range(1, M):
                    nr, nc = r + r1[d]*m, c + c1[d]*m
                    if 0<=nr<N and 0<=nc<N:
                        cnt += arr[nr][nc]
            if cnt > max_fly:
                max_fly = cnt
    # x 검사
            cnt = arr[r][c]
            for d in range(4):
                for m in range(1, M):
                    nr, nc = r + r2[d]*m, c + c2[d]*m
                    if 0<=nr<N and 0<=nc<N:
                        cnt += arr[nr][nc]
            if cnt > max_fly:
                max_fly = cnt

    print(f'#{tc} {max_fly}')
