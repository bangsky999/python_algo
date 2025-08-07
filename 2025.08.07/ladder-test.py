import pprint

arr = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 2, 0],
]  
N = 5
start_r, start_c = -1, -1
for r in range(N):
    for c in range(N):
        if arr[r][c] == 2:
            start_r, start_c = r,c
print(f'({start_r}, {start_c})에서 탐색 시작 !')

r, c = start_r, start_c # 초기화 (없어도됨)

while r > 0: # r == 1 : true, r == 0 : false

    while arr[r][c-1] == 1:
        c -= 1
        arr[r][c] = 3   
        print('break 썼을때')
        
    
    r -= 1
    arr[r][c] = 3
pprint.pprint(f'{r}, {c}, {arr}')
    
#     if arr[r][c-1] == 1:
#         c -= 1
#         arr[r][c] = 3
#         break

# """
#     while arr[r][c-1] == 1:
#         c -= 1
#         arr[r][c] = 3
# """

