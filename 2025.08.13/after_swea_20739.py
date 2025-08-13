import sys; sys.stdin = open("input.txt")
'''
음 행 우선 순회,, 
'''

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0 # 최댓값
    cnt = 0 # 계속 비교할 값

    # 가로 검색
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1: #1이라면 
                cnt += 1
            else: # arr[r][c] = 0이라면
                if cnt > max_cnt:
                    max_cnt = cnt
                cnt = 0 # 0이니까 cnt초기화
            if c == M-1:
                if cnt > max_cnt:
                    max_cnt = cnt
                cnt = 0 # 0이니까 cnt초기화

    # 세로 검색
    # arr[r][c]는 고정인데, for문의 순서만 바꾸기
    for c in range(M):
        for r in range(N):
            if arr[r][c] == 1: #1이라면 
                cnt += 1
            else: # arr[r][c] = 0이라면
                if cnt > max_cnt:
                    max_cnt = cnt
                cnt = 0 # 0이니까 cnt초기화
            if r == N-1:
                if cnt > max_cnt:
                    max_cnt = cnt
                cnt = 0 # 0이니까 cnt초기화
    if max_cnt == 1: # 구조물의 길이가 1이라면 0으로
        max_cnt = 0
    print(f'#{tc} {max_cnt}')