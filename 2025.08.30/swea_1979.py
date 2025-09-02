'''
행, 열 순회를 하자!
1. 각 순회를 하면서 배열의 값이 연속된 1이면 cnt += 1을 하자
2. 검사는 0에서 하자
3. 그럼 끝의 줄에서 k=3이되는 경우는 count안되기에 끝에서도 검사하자
'''
T = int(input())
# T = 1
for tc in range(1, T+1):
    N, K = map(int, input().split()) # N:5, K:3
    arr = [list(map(int, input().split())) for _ in range(N)]
    real_cnt = 0 # 길이가 K인 개수
    # 가로 탐색
    for r in range(N):
        cnt = 0 # K가 있는지 찾을 cnt
        for c in range(N):
            if arr[r][c] == 1: # 흰색이면
                cnt += 1
            elif arr[r][c] == 0: # 검은색이면 검증을 하겠다. 초기화와
                if cnt == K:
                    real_cnt += 1
                cnt = 0
            if c == N-1: # c가 끝에 왔을때
                if cnt == K:
                    real_cnt += 1
                cnt = 0
    # 세로 탐색
    for c in range(N):
        cnt = 0 # K가 있는지 찾을 cnt
        for r in range(N):
            if arr[r][c] == 1: # 흰색이면
                cnt += 1
            elif arr[r][c] == 0: # 검은색이면 검증을 하겠다. 초기화와
                if cnt == K:
                    real_cnt += 1
                cnt = 0
            if r == N-1: # c가 끝에 왔을때
                if cnt == K:
                    real_cnt += 1
                cnt = 0
    
    print(f'#{tc} {real_cnt}')