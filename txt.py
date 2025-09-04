# 10진수를 2진수로 변환
'''
2진수를 문자열로 출력하자
빈 문자열을 만들고 입력받은 10진수를 계속 2로 나누며 문자열에 추가
'''
def decimal_to_binary(n):
    binary_num = ''
    if n == 0:
        return '0'
    
    while n > 0:
        remain = n % 2
        binary_num = str(remain) + binary_num

        n = n // 2
    
    return binary_num

print(decimal_to_binary(144))


# 2진수를 10진수로 변환
'''
문자열을 숫자로 출력하자
how? 2의 ~승 곱해서 0부터 
'''
def binary_to_decimal(bin_num):
    decimal = 0
    pow = 0

    for i in reversed(bin_num): # 1 0 1 1 1
        if i == '1':
            decimal += 2 ** pow

        pow += 1

    return decimal

print(binary_to_decimal('11101'))