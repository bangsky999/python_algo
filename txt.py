import sys;sys.stdin = open("input.txt")
'''
idx를 증가시키면서 col을 검사
'''
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    visited = [0]*N
    min_sum = float('inf')

    def f(idx, cost):
        global min_sum, visited
        # 종료 조건
        if idx == N:
            min_sum = min(cost, min_sum)
            return
        
        # 가지치기
        if cost >= min_sum:
            return
        
        # 유도조건
        for num in range(N):
            if visited[num]:
                continue
            
            # 방문하지 않았다면
            visited[num] = 1
            f(idx + 1, cost + arr[idx][num])
            visited[num] = 0

    f(0, 0)
    print(f'#{tc} {min_sum}')