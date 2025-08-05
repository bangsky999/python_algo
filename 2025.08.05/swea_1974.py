T = int(input())

for tc in range(1, T+1):
    sudoku = []
    for i in range(9):
        lst = list(map(int, input().split()))
        sudoku.append(lst)
    value = 1 # 검증 결과값
    
    for i in range(9):
        line_sum = 0
        for j in range(9):
            ### 세로 합검증
            line_sum += sudoku[j][i]
        if line_sum == 45:
            pass
        else:
            value = 0
            

    for i in range(9):
        line_sum = 0
        for j in range(9):
            ### 가로 합검증
            line_sum += sudoku[i][j]
        if line_sum == 45:
            pass
        else:
            value = 0


        
    for i in [1,4,7]:
        line_sum = 0
        for j in [1,4,7]:
            ### 블록 검증
            line_sum = sudoku[i-1][j-1]+sudoku[i][j-1]+sudoku[i+1][j-1]+sudoku[i-1][j]+sudoku[i][j]+sudoku[i+1][j]+sudoku[i-1][j+1]+sudoku[i][j+1]+sudoku[i+1][j+1]

        if line_sum == 45:
            pass
        else:
            value = 0

    print(f'#{tc} {value}')