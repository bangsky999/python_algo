import sys; sys.stdin = open("input.txt")

def pal(txt): # 회문검사
    val = 0
    for i in range(len(txt)):
        check1 = txt[i]
        check2 = txt[-i-1]
        if check1 == check2:
            val = 1
        else: 
            val = 0
            break
            
    if val == 1:
        return txt
        
for tc in range(1, 11):
    N = int(input())
    arr = [input() for _ in range(8)]
    cnt = 0
    # 가로검사
    for r in range(8):
        for c in range(8-N+1):
            slice = arr[r][c:c+N]
            if slice == pal(slice):
                cnt += 1
    # 세로검사 : 세로 슬라이싱 주의! 안됨 ! 문자열로 합할것
    for r in range(8-N+1):
        for c in range(8):
            slice = ''
            for k in range(N):
                slice += arr[r+k][c]
            if slice == pal(slice):
                cnt += 1
    '''
    # 이거 어떡하지?????
    # for c in range(8):
    #     for r in range(8 - N + 1):
    #         slice = arr[c][r:r+N]
    '''
            

    print(f'#{tc} {cnt}')