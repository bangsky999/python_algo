# 미로의 거리 - BFS
from collections import deque
import sys;sys.stdin=open("input.txt")
'''
최소의 거리 구하는 문제, BFS, queue 사용(deque)
- 2차원 순회를 통해서 시작점 '2'의 좌표를 찾자 -> 시작점을 queue에 넣는다
- 방문 배열 만들기(2차원 배열)
- 2부터 시작해서 4방향 탐색
    - 범위 안에 있고, not visited이면
    - 0이고 이동하고 cnt 추가
        - queue에 추가하기
    - 3이면 찾았다 !
'''
dr = [-1,0,1,0]
dc = [0,1,0,-1]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                start_r, start_c = r, c

    q = deque()
    visited = [[False]*N for _ in range(N)]
    q.append((start_r, start_c,0)) # 4,3
    visited[start_r][start_c] = True
    result = 0

    while q:
        r, c, cnt = q.popleft() # 4, 3
        for d in range(4):
            nr,nc = r+dr[d],c+dc[d]
            if 0<=nr<N and 0<=nc<N:
                if arr[nr][nc] == 0 and not visited[nr][nc]:
                    q.append((nr,nc,cnt + 1))
                    visited[nr][nc] = True
                if arr[nr][nc] == 3: # 찾았다.
                    result = cnt
                    break
    print(f'#{tc} {result}')