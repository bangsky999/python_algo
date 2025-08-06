import sys
sys.stdin = open("input.txt")

# 십자
dr1 = [-1,0,0,1]
dc1 = [0,-1,1,0]
# 대각
dr2 = [-1,-1,1,1]
dc2 = [-1,1,-1,1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_fly = 0 # 최대 파리 수(출력할 것)

    for r in range(N):
        for c in range(N):
            s1 = 0 # 십자 회당 파리 수 측정
            s2 = 0 # 대각 회당 파리 수 측정
            s1 += arr[r][c]
            s2 += arr[r][c]
            # M배 스프레이 키우기
            for i in range(1, M):
                for d in range(4):
                    nr, nc = r + i*dr1[d], c + i*dc1[d]
                    if 0<=nr<N and 0<=nc<N:
                        s1 += arr[nr][nc]

            for i in range(1, M):
                for d in range(4):
                    nr, nc = r + i*dr2[d], c + i*dc2[d]
                    if 0<=nr<N and 0<=nc<N:
                        s2 += arr[nr][nc]



            if max_fly < max(s1,s2):
                max_fly = max(s1,s2)

    print(f'#{tc} {max_fly}')