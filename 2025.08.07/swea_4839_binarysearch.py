import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    l = 1
    r = P
    cnt_A, cnt_B = 0, 0
    while l <= r:
        c = (l+r)//2

        if c == A:
            break
        elif c > A:
            r = c
            cnt_A += 1
        elif c < A:
            l = c
            cnt_A += 1
    l = 1
    r = P
    while l <= r:
        c = (l+r)//2

        if c == B:
            break
        elif c > B:
            r = c
            cnt_B += 1
        elif c < B:
            l = c
            cnt_B += 1

    if cnt_A == cnt_B:
        print(f'#{tc} 0')
    else:
        if min(cnt_A, cnt_B) == cnt_A:
            print(f'#{tc} A')
        else:
            print(f'#{tc} B')
    