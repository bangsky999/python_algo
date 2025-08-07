# 이진 탐색
# l = 1, r = 400, c = (l+r_//2), 찾는 쪽 번호와 c가 같아지면 탐색 종료
# A, B를 따로 만들고 카운트를 해서 마지막에 비교하자
# 이진검색으로 A를 검사하자 -> for문 vs while -> 정해진 횟수보단 값을 찾을때까지 -> while 문이 좋다
# 각 검사마다 초기화할 것 -> l, r
# c와 A값을 비교하자
# c == A라면 찾았다!
# c < A라면 l을 c로
# c > A라면 r을 c로
import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    l, r = 1, P
    cnt_A, cnt_B = 0, 0
    # A검사
    while l <= r:
        c = (l+r)//2
        if c == A:
            break # 찾았다
        elif c < A:
            l = c
            cnt_A += 1
        elif c > A:
            r = c
            cnt_A += 1

    # B검사
    l, r = 1, P
    while l <= r:
        c = (l+r)//2
        if c == B:
            break # 찾았다
        elif c < B:
            l = c
            cnt_B += 1
        elif c > B:
            r = c
            cnt_B += 1

    # 작은 놈 출력하기, 같다면 0내기
    if cnt_A == cnt_B:
        print(f'#{tc} 0')
    else:
        if min(cnt_A, cnt_B) == cnt_A:
            print(f'#{tc} A')
        else:
            print(f'#{tc} B')