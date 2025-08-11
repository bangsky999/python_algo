T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    stop_station = list(map(int, input().split()))

    idx = 0
    cnt = 0

    while idx<N:
        candidates = []
        for s in stop_station:
            if idx <s <=idx+K:
                candidates.append(s)

        if idx+K >= N:





