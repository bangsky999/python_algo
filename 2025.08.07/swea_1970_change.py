# import sys
# sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [0]*8 # [0,0,0,0,0,0,0,0] index - 0:5만, 1:만, 2:오천, 3:천, 4:오백, 5:백, 6:오십, 7:십

    if N // 50000 > 0:
        a = N//50000
        lst[0] = a
        N = N - (50000*a)
    if N // 10000 > 0:
        b = N//10000
        lst[1] = b
        N = N - (10000*b)
    if N // 5000 > 0:
        c = N//5000
        lst[2] = c
        N = N - (5000*c)
    if N // 1000 > 0:
        d = N//1000
        lst[3] = d
        N = N - (1000*d)
    if N // 500 > 0:
        e = N//500
        lst[4] = e
        N = N - (500*e)
    if N // 100 > 0:
        f = N//100
        lst[5] = f
        N = N - (100*f)
    if N // 50 > 0:
        g = N//50
        lst[6] = g
        N = N - (50*g)
    if N // 10 > 0:
        h = N//10
        lst[7] = h
        N = N - (10*h)
    
    print(f'#{tc}')
    for i in lst:
        print(i, end = ' ')
    print()