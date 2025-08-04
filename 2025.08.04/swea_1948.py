T = int(input())
cal = [0,31,28,31,30,31,30,31,31,30,31,30,31] # 월 계산을 위해 0 index 추가
for tc in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    result = 0
    for i in range(m1, m2):
        result += cal[i]
    res = result - d1 + 1 + d2
    print(f'#{tc} {res}')