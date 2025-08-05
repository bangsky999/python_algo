T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for k in range(N):
        lst = list(map(int, input().split()))
        arr.append(lst)
    # 배열 끝~
    max_fly = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            fly_sum = 0
            for m in range(i, i+M):
                for n in range(j, j+M):
                    fly_sum += arr[m][n]


            if fly_sum > max_fly:
                max_fly = fly_sum

    print(f'#{tc} {max_fly}')