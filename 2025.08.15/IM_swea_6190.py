### 정곤이의 단조 증가하는 수 ###
'''
리스트의 앞부터 단조증가 확인 -> [0]번 인덱스 pop하자
맞으면 그걸 바로 정답으로 꺼내고
아니면 다음 번호로
'''

import sys; sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split())) # [2, 4, 7, 10]
    a = len(arr) # a = 4

    multiply_list = []

    for i in range(a-1):
        for j in range(i+1, a):
            mul = arr[i] * arr[j]
            multiply_list.append(mul) 

    # multiply_list = [70, 40, 28, 20, 14, 8]
    multiply_list.sort(reverse=True)
    
    for num in multiply_list:
        s = str(num)
        for k in range(len(s)-1):  # 감소가 있으면 
            if int(s[k]) > int(s[k+1]):
                break
        else:
            print(f'#{tc} {num}') # break 없이 감소가없으면
            break
    else: # 모두 탐색했는데 단조증가가 없다
        print(f'#{tc} -1')