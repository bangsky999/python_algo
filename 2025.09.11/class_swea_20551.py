# 20551. 증가하는 사탕 수열
'''
A<=B<=C의 수열을 만들기 위해 최소의 사탕 eat
1. A<1 and B<2 and C<3이면 불가능

빼서 만들자
- B>=C이면 B = C-1
- A>=B이면 A = B-1

기본 사탕은 0으로 놓고 시작하자, 불가능은 -1 
'''
import sys;sys.stdin=open("input.txt")

T = int(input())
for tc in range(1,T+1):
    A, B, C = map(int,input().split())

    cnt = 0 # 먹을 사탕의 수

    if A<1 or B<2 or C<3: # 불가능한 조건
        print(f'#{tc} -1')
        continue

    # 위의 조건이 아니면
    if B >= C:
        cnt += B - (C - 1)
        B = C-1

    if A >= B:
        cnt += A - (B - 1)
        A = B-1


    print(f'#{tc} {cnt}')