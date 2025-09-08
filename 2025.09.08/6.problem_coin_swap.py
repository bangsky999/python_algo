# 문제 - 동전의 최소 개수
# 규칙 : 큰 동전부터 나누자
coin_list = [100, 50, 500, 10]
target = 1730
result = 0

# greedy 문제의 단골 손님
coin_list.sort(reverse=True)

for coin in coin_list:
    possible_cnt = target // coin# 현재 동전으로 가능한 최대 수
    # 정답에 더해준다
    result += possible_cnt
    
    target -= coin * possible_cnt # 금액을 빼준다.

print(result)

