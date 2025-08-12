'''
풍선을 터트리면 가로 세로 모두를 합하자 r, c
cnt = arr[r][c]
cnt += arr 방향벡터 (구간 설정 !)1 ~4 칸범위
max_cnt 설정
'''
import sys; sys.stdin = open("input.txt")

# + 방향벡터
r1 = [-1,0,0,1]
c1 = [0,-1,1,0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    for r in range(N):
        for c in range(N):
            cnt = arr[r][c]

            for d in range(4):
                for m in range(1,N):
                    nr,nc = r + r1[d]*m, c + c1[d]*m       
                    if 0<=nr<N and 0<=nc<N:
                        cnt += arr[nr][nc]

            if cnt > max_cnt:
                max_cnt = cnt
    
    print(f'#{tc} {max_cnt}')
