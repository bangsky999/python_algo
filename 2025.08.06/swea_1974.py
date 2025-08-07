# import sys
# sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    value = 1

    # 검증 1 
    for r in range(9):
        test_set = set()
        for c in range(9):
            test_set.add(arr[r][c])
        if len(test_set) == 9:
            pass
        else:
            value = 0
            
    
    # 검증 2
    for r in range(9):
        test_set = set()
        for c in range(9):
            test_set.add(arr[c][r])
        if len(test_set) == 9:
            pass
        else:
            value = 0
            

    # 검증 3
    dr = [-1,-1,-1,0,0,1,1,1]
    dc = [-1,0,1,-1,1,-1,0,1]
    for r in [1,4,7]:
        test_set = set()
        for c in [1,4,7]:
            test_set.add(arr[r][c])
            for d in range(8):
                nr, nc = r + dr[d], c + dc[d]
                test_set.add(arr[nr][nc])
            if len(test_set) == 9:
                pass
            else:
                value = 0
                

    print(f'#{tc} {value}')