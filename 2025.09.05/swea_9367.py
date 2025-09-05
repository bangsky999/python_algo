### 9367. 점점 커지는 당근의 개수 ### 
import sys; sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 5
    carrot = list(map(int, input().split())) # [1,2,3,4,5]

    cnt = 1
    max_cnt = 1
    for i in range(N-1): # 0 1 2 3
        if carrot[i+1] > carrot[i]:
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
        else:
            cnt = 1

    print(f'#{tc} {max_cnt}')

