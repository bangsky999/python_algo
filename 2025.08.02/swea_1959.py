T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst_a = list(map(int, input().split()))
    lst_b = list(map(int, input().split()))
    
    if len(lst_a) > len(lst_b):
        short = lst_b
        long = lst_a
    else: 
        short = lst_a
        long = lst_b
    max_num = 0
    for i in range(len(long)-len(short)+1):
        total = 0
        for j in range(len(short)):
            total += short[j] * long[i+j]
        if total > max_num:
            max_num = total
    print(f'#{tc} {max_num}')