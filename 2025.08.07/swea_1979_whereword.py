import sys
sys.stdin = open("input.txt")
'''
고려해야할것
1. 1이면 cnt += 1을 해서 카운트
2. 0을 만났을 때 cnt == K라면 real_cnt += 1
3. 경계에 있을 경우 0을 만나지 않기 떄문에 추가로 cnt 카운트
'''
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    real_cnt = 0 # 빈칸 개수랑 단어 수랑 맞을때 카운트
    
    # 가로 검색
    for r in range(N):
        cnt = 0
        for c in range(N):
            if arr[r][c] == 1: #흰색
                cnt += 1
            else: # 0 -> 검은색이라면???
                if cnt == K: # 단어 수 만족
                    real_cnt += 1 # 
                cnt = 0
            if c == N-1: # 경계일 때
                if cnt == K: # 단어 수 만족
                    real_cnt += 1 # 
                cnt = 0

    # 세로 검색
    for r in range(N):
        cnt = 0
        for c in range(N):
            if arr[c][r] == 1: #흰색
                cnt += 1
            else: # 0 -> 검은색이라면???
                if cnt == K: # 단어 수 만족
                    real_cnt += 1 # 
                cnt = 0
            if c == N-1:
                if cnt == K: # 단어 수 만족
                    real_cnt += 1 # 
                cnt = 0

    print(f'#{tc} {real_cnt}')