'''
- 돌의 인덱스는 0이 아닌 1부터 시작 -> i = i - 1 해야 실제 인덱스
- 돌이 범위를 나갔다면 break로 그만하기
- 값이 0이든 1이든 1-(값)하면 반전됨
'''
import sys; sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N:돌의 수, M:뒤집기 수 -> 뒤집기 수만큼 for문이 나중에 필요
    arr = list(map(int, input().split()))

    for _ in range(M): # tc1의 경우 M은 1 -> 1회만 실행
        i, j = map(int, input().split()) # i:돌의 위치(-1할것), j = 몇개 뒤집을지
        i -= 1 # i = i - 1해서 실제 인덱스로 만들기

        for k in range(1, 1+j): # 기준점 기준으로 동시에 양쪽에 빼기위해 1이 초기값, j는 몇개까지할지
            left = i - k # 좌측 인덱스 설정
            right = i + k # 우측 인덱스 설정
            
            if 0 > left or right >= N: # left, right 값이 범위를 벗어나면 break
                break
            if arr[left] == arr[right]: # arr의 left, right 값이 같다면
                arr[left] = 1 - arr[left] # 1에서 빼서 뒤집기
                arr[right] = arr[left] # right에 left 값복사
            
    print(f'#{tc}', *arr)
            