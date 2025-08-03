T = int(input())
for i in range(1, T + 1):
    price_a = 0
    price_b = 0
    # 9 100 20 3 10 를 입력 받을 때는 map(int, input().split())

    P, Q, R, S, W = map(int, input().split())
    price_a = P * W
    if W <= R:
        price_b = Q
    else:
        price_b = Q + S * (W-R)
    result = min(price_a, price_b)
    print(f'#{i} {result}')

