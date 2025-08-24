### 1210. [S/W 문제해결 기본] 2일차 - Ladder1 ###
'''
0. r=99일때 index를 찾자 -> index메서드 사용
   시작은 arr[99][c]에서 시작
1. 언제까지 올라올지 모르니까 while 사용, 탈출 조건은 r = 0일때.
2. 좌우 체크먼저
    좌가 범위안에 있고 1이라면 
        계속 -1 하기 -> while
3. 위로 올라와라
    - r = r -1 하기
'''
import sys; sys.stdin = open("input.txt")

T = 10
for tc in range(1, T+1):
    input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    r = 99
    c = arr[99].index(2)
    
    while r > 0: # r이 0보다 큰 동안 실행
        if 0 < c and arr[r][c-1] == 1:
            while 0 < c and arr[r][c-1] == 1:
                c = c - 1
        elif c < 99 and arr[r][c+1] == 1:
            while c < 99 and arr[r][c+1] == 1:
                c = c + 1

        r -= 1

    print(f'#{tc} {c}')
