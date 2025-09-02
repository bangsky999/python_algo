### 개미 ###
w, h = map(int, input().split()) # w: 6, h: 4 -> grid
p, q = map(int, input().split()) # p: 4, q: 1 ->초기위치 /// y,x로바꿔
use_p, use_q = q, p # 1,4로 시작하겠다.
t = int(input()) # t시간 후 개미의 위치는?

c = 0 # 현재 시간
cur_r, cur_c = 1, 1
while c != t : # c가 t가 되기 전까지 하겠다
    c += 1
    if use_p != 0 and use_p != h and use_q != 0 and use_q != w:
        use_q += cur_c
        use_p += cur_r
    else: # 벽이라면
        if use_p == 0 or use_p == h:
            cur_r = - cur_r
            use_q += cur_c
            use_p += cur_r
        elif use_q == 0 or use_q == w:
            cur_c = - cur_c
            use_q += cur_c
            use_p += cur_r
print(f'{use_q} {use_p}')
    