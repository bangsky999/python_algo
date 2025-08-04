T = int(input())
for i in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_num = arr[0]
    max_num = arr[0]
    for j in arr[1:]:
        if j < min_num:
            min_num = j
        elif j > max_num:
            max_num = j
    print(f'#{i} {max_num - min_num}')
