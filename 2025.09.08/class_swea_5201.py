### [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반 ### 
import sys; sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split()) # N: 컨테이너, M:트럭수
    weight = list(map(int, input().split()))
    weight.sort(reverse=True) # [5, 3, 1]
    can_weight = list(map(int, input().split()))
    can_weight.sort(reverse=True) # [8, 3]
    is_in = [0]* len(can_weight) # 이미 물건이 들어있는지 확인할 리스트, 이걸 sum하면됨

    for i in weight: # i = 5 ,3 ,1
        for j in range(len(can_weight)): # j = 8, 3
            if i <= can_weight[j] and is_in[j] == 0: # 
                is_in[j] = i
                break

    print(f'#{tc} {sum(is_in)}')
