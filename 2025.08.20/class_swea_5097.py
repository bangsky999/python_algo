### 회전 ###
'''
원형큐를 사용한다는 느낌???
실제값을 넘기기보단 인덱스를 넘겨보자 

맞는지 검증은 강사님께 !
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split())) # [5527,731,31274]

    i = 1 # 인덱스를 지정
    cnt = 1 # M번 만족하는지 체크 카운트
    while cnt <= M: # cnt가 10이 될떄까지
        i += 1 # 인덱스 더하고
        cnt += 1 # cnt 더해
        if i % N == 0: # i가 인덱스를 넘으면 초기로 돌린다
            i = 0
        if cnt == M:
            print(f'#{tc} {lst[i]}')
            break