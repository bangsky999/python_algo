import sys; sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    t, p = map(str, input().split()) # t는 본문, p는 패턴
    cnt = 0
    for i in range(0, len(t) - len(p) + 1):
        if t[i:i+len(p)] == p:
            cnt += 1
            i += len(p)
        else:
            i += 1
    res = len(t) - len(p)*cnt + cnt
    print(f'#{tc} {res}')