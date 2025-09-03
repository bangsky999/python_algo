### 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2 ###
import sys;sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    N = float(input()) # 0.625
    div = 0.5
    binary_num = ''
    while N != 0: # N이 0이 아닐떄까지 동작 수행
        if N >= div: # 크다면
            N = N - div # 0.125
            binary_num += '1'
        else: # 작다면
            binary_num += '0'
        div = div / 2

        if len(binary_num) > 12:
            break
    if len(binary_num) > 12:
        print(f'#{tc} overflow')
    else: 
        print(f'#{tc} {binary_num}')