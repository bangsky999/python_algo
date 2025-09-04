### 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수 ###

'''
16진수 -> 10진수 -> 2진수
'''
def hexadecimal_to_decimal(hexa_str):
    hexa_num = '0123456789ABCDEF'    
    lst = []
    for i in hexa_str: # '4 7 F E'
        aaa = hexa_num.index(i) # 4
        lst.append(aaa) # [4,7,15,14]
    
    return lst

def decimal_to_binary(n):
    binary_number = ''
    if n == 0:
        return '0'
    
    while n > 0:
        remain = n % 2
        binary_number = str(remain) + binary_number

        n = n // 2

    return binary_number

T = int(input())
for tc in range(1,T+1):
    N, string = input().split()
    bb = hexadecimal_to_decimal(string) # [4,7,15,14]
    plus = ''
    for i in bb:
        bin_str = decimal_to_binary(i)
        if len(bin_str) == 1:
            plus = plus + '000'+ bin_str
        elif len(bin_str) == 2:
            plus = plus + '00'+ bin_str
        elif len(bin_str) == 3:
            plus = plus + '0'+ bin_str
        else:
            plus = plus + bin_str

    print(f'#{tc} {plus}')


