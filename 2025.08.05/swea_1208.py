for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        idx_max = arr.index(max(arr))
        arr[idx_max] -= 1
        idx_min = arr.index(min(arr))
        arr[idx_min] += 1
        
    print(f'#{tc} {max(arr) - min(arr)}')