# ### 진기의 최고급 붕어빵 ### 맛있겠다.
# '''
# 3의 배수일 때 +1 하고 i +1, i+2에도 똑같이 더해주기

# hoho_list = [0] * 10
# for i in range(len(hoho_list)):
#     if i % 3 == 0:
#         for j in range(i, len(hoho_list)):
#             hoho_list[j] += 1
# print(hoho_list)
# '''
# import sys; sys.stdin = open("input.txt")
#     # 3초에 가져가면 어떡하지 범위가 2일때..? => 앞으로 순회해서 바뀌는 순간까지 -1 하기
# T = int(input())
# for tc in range(1, T+1):
#     N, M, K = map(int, input().split()) # N: N명, M: M시간 당, K: K개 붕어빵 만든다
#     time = list(map(int, input().split()))
#     time.sort() # sort를 안해도됨 이유는?? 이미 초마다 정해져있어 바로 추가되서 노상관

#     hoho_list = [0]*(max(time)+1)
#     for i in range(1, len(hoho_list)): # 타임라인 별 붕어빵 개수 리스트 [0,0,0,0,0,0,0,0,97] 0초부터
#         if i % M == 0:
#             for j in range(i, len(hoho_list)):
#                 hoho_list[j] += K

#     for i in time:
#         if hoho_list[i] == 0: # 붕어빵이 없다면
#             print(f'#{tc} Impossible')
#             break
#         else: # 붕어빵이 있어
#             back_time = hoho_list[i::-1]
#             for j in range(len(back_time)-1): # 거꾸로 순회하며 숫자가 바뀌는지 체크
#                 if back_time[j] != back_time[j+1]:
#                     for k in range(i-j,len(hoho_list)):
#                         hoho_list[k] -= 1
#                     break
            
#     else: print(f'#{tc} Possible')






T = int(input())
 
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    customers = list(map(int, input().split()))
 
    customers.sort()
    result = 'Possible'
 
    for i in range(len(customers)):
        bread = (customers[i]//M) * K # 손님이 온 시간에 빵 구하는 공식
        if i + 1 > bread:        # 손님은 0명일 수 없으므로 1부터 카운팅해서 손님 수 보다 빵이 적어지면 불가능
            result = 'Impossible'
     
    print(f'#{t} {result}')