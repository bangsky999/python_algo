T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    min_tot = 0 # 충분히 큰 수 
    max_tot = 0 # 충분히 작은 수
    for i in range(N-M+1): # 크게 그룹화
        sum = 0 # 초기 sum 값
        for j in range(i, i+M): # 블록 정해주기
            sum += arr[j]
        if i == 0: # 초기값을 min, max 저장
            min_tot = sum
            max_tot = sum
        if sum < min_tot:
            min_tot = sum
        elif sum > max_tot:
            max_tot = sum

    print(f'#{tc} {max_tot - min_tot}')