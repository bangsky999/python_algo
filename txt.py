from collections import deque
dr = [-1,1,0,0]
dc = [0,0,-1,1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[int(n) for n in input()] for _ in range(N)]
    visited = [[False]*N for _ in range(N)] # 2차원 배열의 방문처리

    # 먼저 3, 2를 찾자
    start_r, start_c, end_r, end_c = -1, -1, -1, -1
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                start_r, start_c = r, c
            elif arr[r][c] == 3:
                end_r, end_c = r, c

    # 큐로 문제 해결 !
    # - 시작점을 큐에 넣고 꺼낸다, 방문처리
    # - 큐가 있다면 while 반복문
    #   -> 주변 탐색 후 if 값 == 0 and not visited
    #       큐에 넣는다
    #   -> if 값 == 3이면 찾았다 !
    q = deque() # 큐를 만든다
    visited[start_r][start_c] = True
    q.append((start_r, start_c, 0))
    result = 0

    while q: # 큐가 있다면 꺼내서 탐색하자
        r, c, level = q.popleft()    
        for d in range(4):            
            nr, nc = r + dr[d], c + dc[d]
            if 0<=nr<N and 0<=nc<N:
                if arr[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr,nc, level + 1))

                if arr[nr][nc] == 3:
                    visited[nr][nc] = True
                    result = level
                    

    print(f'#{tc} {result}')


        
