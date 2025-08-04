T = int(input())
for i in range(1, T+1):
    N, K = map(int, input().split())
    lst = []
    lst2 = [0]*(N+2)
    lst.append(lst2)
    for j in range(N):
        lst1 = [0] + list(map(int, input().split())) +[0]
        lst.append(lst1)
    lst3 = [0]*(N+2)
    # 리스트 만들기 끝~~
    total = 0
    
    for k in range(N-k+3): # 
        for l in range(N-k+3):
            if lst[l][k] ==0 and lst[l][k+1] ==1 and sum(lst[l][k+1:k+K+2]) == K:
                total += 1
            elif lst[k][l] ==0 and lst[k][l+1] ==1 and sum(lst[k][l:l+K+1]) == K:
                total += 1
    print(f'#{i} {total}')


    ###############################푸는 중###################