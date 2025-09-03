w, h = map(int, input().split()) # 1, 1
arr = [list(map(int, input().split())) for _ in range(h)]
visited = [[0]*w for _ in range(h)]
cnt = 0
dc = [0,1,1,1,0,-1,-1,-1]
dr = [-1,-1,0,1,1,1,0,-1]
for r in range(h):
    for c in range(w):
        if arr[r][c] == 1:
            # 방문이 없고 8방탐색에 1이 없으면 +1
            for d in range(8):
                nr, nc = r + dr[d], c + dc[d]
                if visited[r][c] == 0 and arr[nr][nc]
            # 방문이 없고 8방에 1이 있으면 ladder처럼 
            # 끝까지 타고가서 방문 표기 +1
            
