T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [False]*N # 열을 썼는지 표시
    min_sum = 10000000000

    def f(idx, cur_sum): 
        global min_sum
        if idx == N:
            if cur_sum < min_sum:
                min_sum = cur_sum
            return
        
        if cur_sum >= min_sum:
            return
        
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                f(idx+1, cur_sum + arr[idx][i])
                visited[i] = False

    f(0,0)
    print(f'#{tc} {min_sum}')