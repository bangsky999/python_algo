import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    max_cnt = 0 # 최대 1의 개수
    cnt = 0 # 1이 보인다면 카운트

    # arr 순회
    for i in arr:
        if int(i) == 1: # i가 1이라면 cnt에 1을 추가하겠다
            cnt += 1
        else: # i가 0이라면 cnt와 max_cnt를 비교하겠다, 비교 후 cnt 초기화
            if cnt > max_cnt:
                max_cnt = cnt
            cnt = 0
        if arr[-1] == 1: # arr의 마지막 값이 1이라면
            if cnt > max_cnt: # cnt, max_cnt 비교
                max_cnt = cnt
    print(f'#{tc} {max_cnt}')
