import sys; sys.stdin = open("input.txt")

# 1번 풀이
T = int(input())
for tc in range(1, T+1):
    s = list(input())
    val = 1 # while문 탈출값
    i = 0 # 초기 i값

    while val == 1: # val이 1인동안 실행
        if i < len(s)-1:
            if s[i] == s[i+1]:
                s.pop(i+1) # 순서가 꼬이지 않게 뒤에서 pop
                s.pop(i) # 원래 자리 pop
                i = -1 # 자리 돌려주기
            i += 1 # 그다음 글자 넘어가기
        else:
            val = 0 # 끝으로왔다면 val = 0 -> 탈출 조건
    print(f'#{tc} {len(s)}')

# 2번 풀이
def del_word(txt):
    val = 0
    idx = -1
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            val = 1
            idx = i
            break

    if val == 1:
        return del_word(txt[:idx]+txt[idx+2:]) # 재귀함수, 슬라이싱
    else:
        return txt
    
T = int(input())
for tc in range(1, T+1):
    txt = list(input())
    ans = del_word(txt)
    print(f'#{tc} {len(ans)}')