def bruteforce(p,t): 
# p 찾을 패턴, t 본문 문자열, 패턴이 있으면 인덱스, 없으면 -1 리턴
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    M = len(p)
    N = len(t)
    while j < M and i < N:
        if t[i] != p[j]: # 만약 문자열이 다르면
            i = i - j # i를 원래 위치로 되돌림
            j = -1 # j는 -1으로 돌림
        i = i + 1 # i의 다음칸
        j = j + 1 # j의 다음칸 
    if j == M: return i - M 
    else: return - 1
    
t = 'TTTTTATTAATA'
p = 'TTA'

print(bruteforce(p, t))