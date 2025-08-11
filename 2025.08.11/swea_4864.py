import sys
sys.stdin = open("input.txt")

def bruteforce(p,t):
# p는 패턴, t는 본문
    i = 0 # t
    j = 0 # p
    M = len(p)
    N = len(t)
    
    while i < N and j < M:
        if t[i] != p[j]:
            i = i -j
            j = -1
        i += 1
        j += 1
    if j == M:
        return 1
    else:
        return 0
    
T = int(input())
for tc in range(1, T+1):
    p = input()
    t = input()
    res = bruteforce(p, t)
    print(f'#{tc} {res}')
