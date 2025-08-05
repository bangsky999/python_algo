T = int(input())

# 문제의 조건이 for문이 아니라 jump 된다면 while문으로 !!

def charging_station(K, N, M, chargers):
    idx = 0
    cnt = 0
    while idx < N:
        candidates = []
        for c in chargers:
            if idx < c <= idx + K:
                candidates.append(c)

        # 예외 조건 찾아내기 !
        if idx + K >= N:
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

