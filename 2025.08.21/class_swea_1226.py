### 1226. [S/W 문제해결 기본] 7일차 - 미로1 ###
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

for tc in range(1, 11):
    t = input()
    arr = [[int(n) for n in input()] for _ in range(16)]

    visited = [[False]*16 for _ in range(16)]

    start_r, start_c = -1, -1
    for r in range(16):
        for c in range(16):
            if arr[r][c] == 2: # 시작점
                start_r, start_c = r, c

    # 1. 큐를 만든다
    q = deque()
    q.append((start_r, start_c)) 
    visited[start_r][start_c] = True
    result = 0

    while q: # q가 있는 동안 동작 수행
        if result == 1:
            break
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0<=nr<16 and 0<=nc<16:
                if arr[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                if arr[nr][nc] == 3: # 찾았다.
                    result = 1
                    break
				

    print(f'#{tc} {result}')