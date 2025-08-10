'''
K칸 이내에 버정이 있어야한다.
없다면? return 0
있으면 그 중 가장 멀리 가야한다.list의 맨뒤값?? 그리고 최소 충전횟수 count

'''

T = int(input())

def charging_station(K,N,M, chargers):
    idx = 0
    cnt = 0
    while idx < N:
        candidates = []
        for c in chargers:
            if idx < c <=idx +K:
                candidates.append(c)
        if idx+K >= N:
            return cnt
        if len(candidates) == 0:
            return 0 
        
        else:
            idx = candidates[-1]
            cnt += 1

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    chargers = list(map(int, input().split()))

    cnt = charging_station(K, N, M, chargers)
    print(f'#{tc} {cnt}')
 
