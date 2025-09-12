# 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용
'''
제품별 생상공장을 다르게
'''
import sys; sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    cost = 0
    min_cost = 99999
    factory = [0]*N # 방문배열

    def f(idx):
        global cost, min_cost

        # 종료조건
        if idx == N:
            if cost < min_cost:
                min_cost = cost
            return
        
        # 가지치기
        if cost >= min_cost:
            return

        # 유도 조건
        for num in range(N):
            if factory[num]: 
                continue
            
            factory[num] = True
            cost += arr[idx][num]
            f(idx+1)
            cost -= arr[idx][num]
            factory[num] = False

        
    f(0)
    print(f'#{tc} {min_cost}')
    