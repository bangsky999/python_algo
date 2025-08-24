### 20551. 증가하는 사탕 수열 ###
'''
A < B < C 가 주어지면 C는 줄일 수 없음
최소가 되려면 A = C -2가 되어야함, B = C - 1
- 언제까지 빼야할지 모르니까 while을 쓰자
탈출조건은 1 <= A < B < C가 될때까지 
'''
import sys; sys.stdin = open("input.txt")


T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    res = 0
    # 여기서는 가능한 조건 -> 나보다 앞에가 크거나 같을때
    while True: # 조건은 나중에 생가
        if A < B < C:
            res = 0
            break
        if C == 1 or C == 2 or B == 1:
            res = -1
            break
        
        # 두개에도 걸리지 않는 경우
        if B >= C: # 
            res += (B - C + 1)
            B = C - 1
            
        if A >= C:
            res += (A - C + 2)
            A = C - 2

        if C - A == 1:
            res += 1
            A = A - 1

        break

    print(f'#{tc} {res}')
    
        