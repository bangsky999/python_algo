N = int(input())
for k in range(1, N+1):
    N, M = map(int, input().split())
    grid = []
    
    for _ in range(N):
        row = list(map(int, input().split()))
        grid.append(row)

    max_num = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            fly_num = 0

            for x in range(M):
                for y in range(M):
                    fly_num += grid[i+x][j+y]
                    
                    if fly_num > max_num:
                        max_num = fly_num
                    
    print(f"#{k} {max_num}")
    