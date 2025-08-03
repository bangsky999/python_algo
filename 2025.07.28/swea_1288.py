# T = int(input())
# for i in range(1, T + 1):
#     N = int(input())
#     s1 = set() # s1 = {}
#     # 집합의 크기가 10 미만일때까지 적용
#     # x로 카운팅할때 range보다는 
#     # x로 카운팅이 좋음
#     x = 0
#     while len(s1) < 10:
#         x += 1
#         num = str(N * x)
#         for j in num:
#             s1.add(j)
#         if len(s1) == 10:
#             break
#     print(f'#{i} {num}')
                




T = int(input())
for i in range(1, T + 1):
    N = int(input())
    x = 0
    s1 = set()
    while len(s1) < 10:
        x += 1
        num = N * x
        for j in str(num):
            s1.add(j)
        if len(s1) == 10:
            break
    print(f'#{i} {num}')