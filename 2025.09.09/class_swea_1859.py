# 백만 장자 프로젝트
'''
내가 뒤에 시세를 알면 정확한 매매를 할 수 있다.-> 뒤에서부터 계산하자
1. 앞 >= 뒤 : 사지마
2. 앞 < 뒤 : 사 ! ,,,ex)1 1 3
'''
import sys;sys.stdin=open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))

    max_price = 0
    profit = 0

    # 뒤에서부터 거꾸로 탐색
    for i in range(N-1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            profit = profit + (max_price - prices[i])
    
    print(f"#{tc} {profit}")