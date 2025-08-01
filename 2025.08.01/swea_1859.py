# 입력
T = int(input())
for i in range(1, T+1):
    # output
    profit = 0
    # 현재 리스트 인덱스의 금액
    current_price = 0
    N = int(input())
    lst = list(map(int, input().split()))
    # 리스트의 마지막을 max_price로 설정
    max_price = lst[-1]
    # 리스트의 마지막을 제외한 -2 ~ 리스트의 첫번쨰까지 순회
    for j in range(2,N+1):
        current_price = lst[-j]
        
        if current_price <= max_price:
            profit += (max_price - current_price)

        else:
            max_price = current_price
            
    print(f'#{i} {profit}')