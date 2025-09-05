### 6190. 정곤이의 단조 증가하는 수 ###
import sys;sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # N:4
    arr = list(map(int, input().split())) # [2,4,7,10]
    arr.sort() # 정렬 후 뒤에서부터 두개씩 계산
    
    res = -1
    max_res = -1
    val = 0 # flag

    for i in range(N-1,0,-1): # 3 2 1
        for j in range(i-1,-1,-1): # 2 1 0
            multiply = str(arr[i] * arr[j]) # '75432'

            for k in range(len(multiply)-1): # 0 1 2 3
                if multiply[k] > multiply[k+1]: 
                    val = 0
                    break
                else:
                    val = 1

            if val == 1:
                res = int(multiply)
                if res > max_res:
                    max_res = res

    
    print(f'#{tc} {max_res}')

            
