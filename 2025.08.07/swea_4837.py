# import sys
# sys.stdin = open("input.txt")

T = int(input())
arr = list(range(1, 13))
for tc in range(1, T+1):
    N, K = map(int, input().split())
    n = len(arr)
    cnt = 0
    ### 이해 좀해라
    for i in range(1<<12):
        lst = []
        for j in range(12):
            if i & (1<<j):
                lst.append(arr[j])
    ###
        if sum(lst) == K and len(lst) == N:
            cnt += 1
    
    print(f'#{tc} {cnt}')
