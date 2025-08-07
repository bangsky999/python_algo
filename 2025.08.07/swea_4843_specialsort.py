import sys
sys.stdin = open("input.txt")


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]: # 부등호 방향에 따라 방향이 바뀌네 ~
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    ### 정렬 완료 ###
    # 반으로 나눠서 
    # 순방형, 역방향을 만들고 i값에 따라 가져오겠다.
    lst1 = arr[:N//2] # / <-기호 사용시 float형이 나와서 int로
    lst2 = arr[N-1:(N//2)-1:-1]
    lst = []
    for i in range(N//2):
            lst.append(lst2[i])
            lst.append(lst1[i])
    print(f'#{tc}', end = ' ')
    for j in lst[:10]:
        print(j, end = ' ')
    print()