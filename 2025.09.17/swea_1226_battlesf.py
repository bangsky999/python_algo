# 1226. [S/W 문제해결 기본] 7일차 - 미로1
import sys;sys.stdin = open("input.txt")
from collections import deque
'''
이 문제의 해답은 DFS, BFS가 될 수 있음
- DFS: 재귀호출, stack(나는 재귀호출은 잘모르고 stack도 잘모르고 있음)
- BFS: Queue를 사용,

1. 2중 for문 순회후 
    - 2: start r, c 좌표 기억
    - 3: end r, c 좌표 기억
2. 이동 가능한 조건
    - 4방탐색한 nr,nc 가 grid 안에 있을때
    - 0일때
    - 방문하지 않았을때
3. 도달한다면, 결과 1, 아니면 0
'''
dr = [-1,1,0,0]
dc = [0,0,-1,1]

T = 10
for tc in range(1,T+1):
    input()
    arr = [[int(i) for i in input()] for _ in range(16)]
    
    # 2, 3을 찾자
    for r in range(16):
        for c in range(16):
            if arr[r][c] == 2:
                start_r, start_c = r, c
            if arr[r][c] == 3:
                end_r, end_c = r,c 
    
    # visited 배열
    visited = [[0]*16 for _ in range(16)]
    result = 0

    q = deque()
    q.append((start_r, start_c))
    visited[start_r][start_c] = 1

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0>nr or nr>=16 or 0>nc or nc>=16:
                continue
            if arr[nr][nc] == 1:
                continue
            if visited[nr][nc]:
                continue

            if arr[nr][nc] == 3:
                result = 1
                break
            
            q.append((nr,nc))
            visited[nr][nc] = 1

    print(f'#{tc} {result}')
