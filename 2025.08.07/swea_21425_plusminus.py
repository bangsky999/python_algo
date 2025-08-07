import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    A, B ,N = map(int, input().split())
    cnt = 0
    while A < N or B < N:
        small_num, big_num = min(A, B), max(A, B)
        small_num += big_num
        cnt += 1
        A, B = small_num, big_num
        if max(A, B) < N:
            
        else:
            break
    print(f'{cnt}')

    ##########a 미완 ###