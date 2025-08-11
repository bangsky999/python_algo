import sys
sys.stdin = open("input.txt")

def bruteforce(p,t):
    # p 찾을 패턴, t 본문 문자열
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    M = len(p)
    N = len(t)
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M: # j값은 맞춘 글자 개수가 됨 !
        return 1
        # return i - M
    else:
        return 0 

T = int(input())
for tc in range(1, T+1):
    p = input()
    t = input()
    res = bruteforce(p, t)
    print(f'#{tc} {res}')