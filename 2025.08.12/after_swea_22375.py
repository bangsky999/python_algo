'''
<전략>
조작 전: before
조작 후: after
1. 앞에서 부터 차례로 인덱스 비교후 다르면, 그 인덱스부터 전부 뒤집기 cnt+1
while문이 편할듯 ? -> 같을때까지 반복하면 되니까, 근데 인덱스를 먹이기 위해 for 사용
1-1. 뒤집기는 1-(값)
2. 그 다음인덱스부터 실행
3. 같으면 출력
* 주의 사항: 인덱스번호가 1번부터 시작(i-1할것)
'''
import sys; sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr_before = list(map(int, input().split()))
    arr_after = list(map(int, input().split()))
    # i = 0 # 시작 인덱스
    cnt = 0 # cnt
    
    # 풀이 1 - while 사용
    # while arr_before != arr_after: # 다를 동안 반복하겠어 !
    #     if arr_before[i] != arr_after[i]: # i번째가 다르다면
    #         for j in range(i, N): # i~ N 까지 바꾸겠어
    #             arr_before[j] = 1 - arr_before[j]
    #         cnt += 1
    #     i += 1

    # 풀이 2 - for문 사용
    for i in range(N):
        if arr_before[i] != arr_after[i]:
            for j in range(i, N):
                    arr_before[j] = 1 - arr_before[j]
            cnt += 1

    print(f'#{tc} {cnt}')