### 피자 굽기 ###
'''
N개의 피자를 동시에 구울수있는 화덕
1~M까지 M개의 피자를 순서대로 화덕에 넣는다, 치즈 녹는 시간이 달라 꺼내는 순서가 달라 !
마지막까지 남은 피자번호를 알아내라 !

피자는 1번에서만 넣거나 뺄수 있음

1번 테케 
N: 3 ,M: 5
7 2 6 5 3
'''

from collections import deque

T = int(input()) # 테스트케이스 수

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheeses = list(map(int, input().split()))
    nums = list(range(1, M+1))

    # (피자번호, 치즈의양) 튜플로 만들기
    # cheeses = [7 2 6 5 3]
    # nums    = [1 2 3 4 5]
    # pizzas  = [(1, 7), (2, 2), (3, 6), (4, 5), (5, 3)]
    pizzas = list(zip(nums, cheeses))


    q = deque() # 화덕의 큐
    # 화덕의 크기는 N이므로 일단 앞의 N개의 피자를 화덕에 집어 넣는다.
    for _ in range(N): # N번 반복
        q.append(pizzas.pop(0)) # 앞에서부터 하나씩 화덕에 집어넣음

    # 종료: 최후의 피자 1개가 남으면 됨 - 목표 상태
    # 반복: 2개 이상이라면 계속 반복   - 목표에 이르지 못한 상태

    while len(q) > 1: # 화덕에 피자가 2개 이상이라면 반복한다
        #  len(q) > 1 == True라면 반복
        # 화덕에서 피자 꺼내기(제일 앞에 있는 피자는 이미 화덕을 한바퀴 돈 상태)
        # 꺼낸 피자는 치즈를 2로 나눠주면 됨
        num, cheese = q.popleft() # 가장 앞에 있는 피자 꺼내기
        cheese //= 2 # 치즈를 반으로 줄여준다

        if cheese == 0 and pizzas: # 만약에 치즈가 0이 되고, 아직 화덕에 넣지 않은 피자가 남아 있다면
            q.append(pizzas.pop(0))
        elif cheese > 0: # 치즈가 아직 0이 아니라면 => 다시 화덕에 넣는다
            q.append((num, cheese))
    
    # while문이 끝났다면 len(q) > 1 == False이면 끝
    #                  len(q) <= 1이 되었다는 뜻
    # 최후의 피자 1개가 남음

    # 최후의 피자 1개를 꺼낸다
    num, cheese = q.popleft()

    print(f"#{tc} {num}") # 최후의 피자 번호를 출력

