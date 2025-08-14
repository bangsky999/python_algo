### 오목 판정 ###
dr = [-1, 0, 1, 1]
dc = [1, 1, 1, 0]

import sys; sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    value = 'NO'
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o': # 돌이 있다면 검사하자
                for d in range(4):
                    lst = [] # 먼저 리스트 만들기
                    cnt = 0
                    for m in range(1,5):
                        nr,nc = r + dr[d]*m, c + dc[d]*m
                        if 0<=nr<N and 0<=nc<N:
                            lst.append(arr[nr][nc])
                    # for i in range(len(lst)):
                        # if lst[i] == 'o':
                        #     cnt += 1
                        a = lst.count('o')
                        print(a)
                    
                    if cnt == 4:
                        value = 'YES'


    print(f'#{tc} {value}')
