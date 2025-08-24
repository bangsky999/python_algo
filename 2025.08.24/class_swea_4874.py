### 4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth ###

T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())

    stack = []
    stack.append(arr.pop(0)) # 10

    while stack:
        a = arr.pop(0)
        if a in ['+', '-', '*', '/']:
            