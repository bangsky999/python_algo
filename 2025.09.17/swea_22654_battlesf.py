# 차윤이의 RC카
import sys;sys.stdin=open("input.txt")
'''
1. 시작점과 끝점을 찾자
2. 방향벡터를 상 우 하 좌 로 설정하고 R이면 +1, L이면 -1로 하자 
    -> 딕셔너리로 만들고 시작값은 1로 한다음 값 + 1 하고 % 4로 한 값으로 하자
  - visited, bfs 이런거는 아닌거같음 풀다 맞으면 추가하자
3. 주어진대로 이동했을 때
    - Y이면 1
    - Y 아니면 0
'''
def check(r, c, C, command, d): 
    global field, dir
    cnt = 0
    result = 0
    while cnt != C:
        if command[cnt] == 'R':
            d = (d + 1) % 4
            cnt += 1
        elif command[cnt] == 'A':
            r = r + dir[d][0]
            c = c + dir[d][1]
            if 0>r or r>=N or 0>c or c>=N or field[r][c] == 'T':
                r = r - dir[d][0]
                c = c - dir[d][1]
            cnt += 1

        elif command[cnt] == 'L':
            d = (d - 1) % 4
            cnt += 1
        
    if field[r][c] == 'Y':
        result = 1
    return result

dir = {0:[-1,0], 1:[0,1], 2:[1,0], 3:[0,-1]}
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    field = [list(input()) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if field[r][c] == 'X':
                sr, sc = r, c 
            if field[r][c] == 'Y':
                er,ec = r, c

    print(f'#{tc}', end = ' ')

    Q = int(input()) # 조종을 한 횟수
    for _ in range(Q):
        C, command = input().split()
        result = check(sr, sc, int(C), command, 0)
        print(f'{result}', end = ' ')
    print()