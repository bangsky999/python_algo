import sys;sys.stdin = open("input.txt")
from collections import deque

dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0: # 0, 0을 받으면 끝 !
        break
    arr = [list(map(int,input().split())) for _ in range(h)]
   
    # 방문처리 배열
    visited = [[0]*w for _ in range(h)]
    cnt = 0

    
    
    for r in range(h):
        for c in range(w):
            if arr[r][c] == 1 and not visited[r][c]:
                q = deque()
                q.append((r,c))
                visited[r][c] = 1
                cnt += 1

                while q:
                    i, j = q.popleft()

                    for d in range(8):
                        nr, nc = i + dr[d], j + dc[d]
                        if 0<=nr<h and 0<=nc<w:
                            if arr[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = 1
                                q.append((nr,nc))
                                

    print(cnt)