### 정곤이의 단조 증가하는 수 ###
import sys; sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split())) # [2, 4, 7, 10]
    a = len(arr) # a = 4

    multiply_list = []
    value = False

    for i in range(a-1):
        for j in range(i+1, a):
            mul = arr[i] * arr[j]
            multiply_list.append(mul) 

    # multiply_list = [8, 14, 20, 28, 40, 70]
---------
        
    
