T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))

    max_price = 0
    profit = 0

    # 뒤에서부터 거꾸로 탐색
    for i in range(N-1, -1, -1):
        # 매수
        if prices[i] > max_price:
            max_price = prices[i]
        # 판매
        else:
            profit = profit + (max_price - prices[i])
    
    print(f"#{tc} {profit}")