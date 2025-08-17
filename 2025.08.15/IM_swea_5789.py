### 현주의 상자 바꾸기 ###
'''
입력받은 i를 추가하는데 인덱스는 1번부터라 생각
'''
import sys; sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split()) # N: 상자의 개수(1~N), Q: i가 1부터 Q까지 돈다
    arr = [0] * N # [0,0,0,0,0]
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L-1, R): # 1 ~ 3 => 0~2
            arr[j] = i
    
    print(f'#{tc}', *arr)