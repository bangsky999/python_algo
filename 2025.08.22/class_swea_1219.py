### 1219. [S/W 문제해결 기본] 4일차 - 길찾기 ###
'''
stack을 가지고 문제를 풀자.
0. 인덱스를 0~99까지 (0,100)까지 만들어서 입력 받은 위치 정보를 각 인덱스에 맞게 집어넣자
1. (0,100)까지 visited를 만들어서 방문처리를 하자
2. 시작점을 스택에 집에넣고 방문처리
3. stack이 있다면~ (while 반복문 처리)
4. stack에서 하나를 꺼내고
4.1 if 그게 향하는 방향이 99면 찾았다.
4.2 if 아니면 다시 인덱스 정보를 찾아서 들어가자
        방문처리도 잘하고
'''
import sys; sys.stdin = open("input.txt")
for tc in range(1, 11):
    T, N = map(int, input().split())
    arr = list(map(int, input().split()))
    forward = [[] for _ in range(100)] # 어디로 향하는지 적을 리스트
    visited = [False]*100
    for i in range(0, N*2, 2):
        forward[arr[i]].append(arr[i+1])
    S, G = 0, 99    

    stack = [] # 스택을 만들고 시작점을 넣는다, 방문표시까지
    stack.append(S)
    visited[S] = True
    result = 0

    while stack: # 스택이 있다면
        v = stack.pop()
        if v == G: # 찾았다면! result 바꿔주고 탈출하자
            result = 1
            break

        for w in forward[v]:
            if not visited[w]:
                visited[w] = True
                stack.append(w)

        
    print(f'#{tc} {result}')