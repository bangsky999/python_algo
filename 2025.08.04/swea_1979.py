T = int(input())
for tc in range(1, T+1):    
    N, K = map(int, input().split())
    
    # 배열 만들기
    lst = []
    for i in range(N):
        lst1 = list(map(int, input().split()))
        lst.append(lst1)
    
    real_cnt = 0
    cnt = 0
    for j in range(N):
        for k in range(N):
            if lst[j][k] == 1:
                cnt += 1
            else:
                if cnt == K:
                    real_cnt += 1
                cnt = 0
            
            if k == N-1:
                if cnt == K:
                    real_cnt += 1
                    cnt = 0
                else:
                    cnt = 0

    for j in range(N):
        for k in range(N):
            if lst[k][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    real_cnt += 1
                cnt = 0
            
            if k == N-1:
                if cnt == K:
                    real_cnt += 1
                    cnt = 0
                else:
                    cnt = 0

    print(f'#{tc} {real_cnt}')
