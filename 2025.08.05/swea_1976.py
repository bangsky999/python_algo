# import sys
# sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    
    # m1 + m2 >60 이면
    if m1 + m2 >= 60:
        # 12시가 넘으면 
        if h1 + h2 >= 12:
            minute = m1 + m2 - 60
            hour = h1 + h2 + 1 - 12
        # 12시가 안넘으면
        else:
            minute = m1 + m2 - 60
            hour = h1 + h2 + 1
            if hour >= 12:
                hour = hour - 12
    # m1 + m2 <60분을 넘지 않으면
    else:
        # 12시가 넘으면
        if h1 + h2 >= 12:
            minute = m1 + m2
            hour = h1 + h2 - 12
        # 12시가 안넘으면
        else:
            minute = m1 + m2
            hour = h1 + h2

    print(f'#{tc} {hour} {minute}')

