'''
s: 본문, p: 패턴
1. in과 슬라이싱을 이용하자, 앞글자만 남기고 len으로 개수 구하기
2. 
'''
import sys; sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    s, p = input().split() # s: banana, p: bana
    cnt = 0 # p가 몇번 나왔니?
    i = 0
    while i <= len(s)-len(p): # p의 길이만큼만 빼고 i를 돌리겠다
        if s[i:i+len(p)] == p:
            cnt += 1
            i += len(p)
        else:
            i += 1
    ans = len(s)-(len(p)*cnt) + cnt

    print(f'#{tc} {ans}')