# 피자굽기 - 시뮬레이션
from collections import deque
import sys;sys.stdin=open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split()) # N:화덕 크기, M: 피자 수
    cheeses = list(map(int,input().split())) # [7,2,6,5,3]
    num_pizzas = [(idx,pizza) for idx, pizza in enumerate(pizzas, start=1)] 
    # [(1, 7), (2, 2), (3, 6), (4, 5), (5, 3)]
    q = deque()
    for i in range(N):
        q.append(num_pizzas.pop(0))
    # print(q) # deque([(1, 7), (2, 2), (3, 6)])
    # print(num_pizzas) # [(4, 5), (5, 3)]

    while True:
        i,j = q.popleft() # (1,7)
        j = j // 2
        if j == 0: # 다먹었으면 비워서 넣자
            if len(q) == 1:
                break
            if num_pizzas:
                q.append(num_pizzas.pop(0))
        else:
            q.append((i,j))
    i,j = q.popleft()
    print(f'#{tc} {i}')