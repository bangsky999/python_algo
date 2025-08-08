import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    A, B ,N = map(int, input().split())
    cnt = 0
    while B <= N:
        A, B = min(A, B), max(A, B) 
        # A = min(A, B)
        # B = max(A, B) 로 하면 a, b = (5,3)일때, (3,3)이 되버림

        
        A += B
        cnt += 1

        B, A = A, B
        if B > N:
            break

    print(f'{cnt}')