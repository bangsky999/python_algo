T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for i in range(1, N+1):
        lst = [1] * i
        arr.append(lst)
        
    for i in range(1, N):
        for j in range(1, N):
            if 