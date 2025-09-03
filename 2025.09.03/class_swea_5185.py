### 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수 ###
'''
16진수를 변환해서 10진수로 바꾼다. 
10진수를 2진수로 바꾸고 list에 append 한다
'''
import sys; sys.stdin = open("input.txt")
hexa_digits = '0123456789ABCDEF'
T = int(input())
def decimal_to_binary(n):
    binary_num = ''
    if n == 0:
        return '0000'
    while n > 0:
        remain = n % 2
        binary_num = str(remain) + binary_num
        n = n // 2
    if len(binary_num) == 1:
        binary_num = '000'+ binary_num
    elif len(binary_num) == 2:
        binary_num = '00'+ binary_num
    elif len(binary_num) == 3:
        binary_num = '0'+ binary_num
    return binary_num    

for tc in range(1, T+1):
    binary_number = ''
    N, hexadecimal_number = input().split() # 4 47FE
    for i in range(int(N)): # 4
        binary_number += decimal_to_binary(hexa_digits.index(hexadecimal_number[i])) # 4 -> '0100'
    print(f'#{tc} {binary_number}')
