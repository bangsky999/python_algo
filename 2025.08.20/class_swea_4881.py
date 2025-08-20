### 순열인데 def부분부터 흐름을 전혀 이해를 못하겠음. ###
'''
강의부터 다시 !!!!!!!!!!!!!!!
'''
T = int(input().strip())
min_sum = 10000000000 # 전역
 
for test_case in range(1, T + 1):
    N = int(input().strip())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    visited = [False] * N   # 열을 썼는지 표시
 
    min_sum = 10000000000
 
    def f(idx, cur_sum): # idx = 행 번호????
        global min_sum
        if cur_sum >= min_sum: # 가지치기->크기만하면 계산할 필요없으니까 자르겠다.
            return 
 
        if idx == N: # 모든행을 다 배정했으면 최소값 갱신
            if cur_sum < min_sum:
                min_sum = cur_sum
            return
        
        # idx번째 행에 어떤 열을 배정할지 시도
        for j in range(N):
            if not visited[j]:           # 아직 안 쓴 열이면
                visited[j] = True        # 사용 표시
                f(idx+1, cur_sum + arr[idx][j])  # 다음 행으로
                visited[j] = False       # 원상복구
 
    f(0, 0)
    print(f"#{test_case} {min_sum}")