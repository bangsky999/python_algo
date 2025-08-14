### 우주 괴물 ###
'''
1. 2번을 포함해서 십자로 1을 만날때까지 1로 덮어쓰기
    1. 2의 배열을 찾고 r,c를 찾아낸다
    2. 거기에 1 덮어쓴다
2. 배열을 순회하면서 0의 갯수를 세면 끝!
'''
import sys; sys.stdin = open("input.txt")
# dr = [-1,0,0,1]
# dc = [0,-1,1,0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                find_r, find_c = r, c
    

    for m in range(1, N):
        # 위 방향
        nr, nc = find_r + (-1)*m, find_c + (0)*m
        if 0<=nr<N and 0<=nc<N: # 범위 내에서
            if arr[nr][nc] == 1:
                break
            else:
                arr[nr][nc] = 3

    for m in range(1, N):
        # 좌 방향
        nr, nc = find_r + (0)*m, find_c + (-1)*m
        if 0<=nr<N and 0<=nc<N: # 범위 내에서
            if arr[nr][nc] == 1:
                break
            else:
                arr[nr][nc] = 3

    for m in range(1, N):
        # 우 방향
        nr, nc = find_r + (0)*m, find_c + (1)*m
        if 0<=nr<N and 0<=nc<N: # 범위 내에서
            if arr[nr][nc] == 1:
                break
            else:
                arr[nr][nc] = 3

    for m in range(1, N):
        # 아래 방향
        nr, nc = find_r + (1)*m, find_c + (0)*m
        if 0<=nr<N and 0<=nc<N: # 범위 내에서
            if arr[nr][nc] == 1:
                break
            else:
                arr[nr][nc] = 3


   
    cnt = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                cnt += 1

    print(f'#{tc} {cnt}')
