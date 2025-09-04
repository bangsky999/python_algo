### [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합 ###
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = float('inf')
    res = [0]*N # [1,2,3]
    visited = [False]*N

    def f(idx, sum):
        global min_sum
        # 종료 조건
        if idx == N:
            if sum < min_sum:
                min_sum = sum
            return
        
        if sum >= min_sum:
            return
        
        # 실제 동작 수행
        for num in range(N):
            if not visited[num]:
                visited[num] = True
                res[num] = num
                f(idx+1, sum +arr[idx][num])
                visited[num] = False


    f(0, 0)
    print(f'#{tc} {min_sum}')