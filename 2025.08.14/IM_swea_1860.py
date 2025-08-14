### 진기의 최고급 붕어빵 ### 맛있겠다.
'''
3의 배수일 때 +1 하고 i +1, i+2에도 똑같이 더해주기
'''
'''
hoho_list = [0] * 10
for i in range(len(hoho_list)):
    if i % 3 == 0:
        for j in range(i, len(hoho_list)):
            hoho_list[j] += 1
print(hoho_list)
'''
import sys; sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split()) #
    client_time = list(map(int, input().spli()))
    client_time.sort()

    hoho_list = [0] * (max(client_time)+1)
    for i in range(len(hoho_list)):
        if i % M == 0:
            for j in range(i, len(hoho_list)):
                hoho_list[j] += K

    # 3초에 가져가면 어떡하지 범위가 2일때..?