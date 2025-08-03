T = int(input())
for i in range(1, T+1):
    N = int(input()) # 5
    lst = list(range(1, N+1)) # [1,2,3,4,5]
    # lst 길이만큼 인덱싱을 해서
    for j in range(len(lst)):
        # 
        if lst[j] % 2 == 0:
            lst[j] = -(j+1)
    result = sum(lst)
    print(f'#{i} {result}')