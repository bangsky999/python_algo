### 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로 ###

'''
stack으로 미로 탈출 어떻게 할 수 있을까?
stack의 구조 선입 후출 -> 먼저 들어온게 늦게 나감
먼저 2를 2차원 순회를 통해 찾는다, 방문처리만들기
1. 스택에 시작점을 넣고 방문처리
2. while 설정 -> 조건: stack이 있으면
3. 상하좌우 순회하며 값 == 0 and not visited일 경우 가기
4. 값 == 3이면 찾았다.
'''
# import sys; sys.stdin = open("input.txt")
dr = [-1,1,0,0]
dc = [0,0,-1,1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                start_r, start_c = r, c
    
    visited = [[False]*N for _ in range(N)]

    stack = []
    stack.append((start_r,start_c))
    visited[start_r][start_c] = True
    result = 0

    while stack:
        r, c = stack.pop()           
        for d in range(4):          
            nr, nc = r + dr[d], c + dc[d]
            if 0<=nr<N and 0<=nc<N:
                if arr[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    stack.append((nr,nc))
                elif arr[nr][nc] == 3:
                    result = 1
                    break
    
    print(f'#{tc} {result}')