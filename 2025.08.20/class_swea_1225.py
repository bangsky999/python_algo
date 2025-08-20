### 암호 생성기 ###
'''
원형큐네 why? 선형 큐는 앞으로 당기는건데 비효율적
맨앞의 인덷ㄱ스를 가져와서 pop해서 맨뒤로 보내 그리고 -i만큼 (i는 1~5)
deque쓰면 될거같은데
맨 뒤로 가는 숫자가 <= 0이 종료 조건 아 while이 좋겠다.
'''
for _ in range(10):
    tc = int(input())
    password_lst = list(map(int, input().split()))
    flag = 0

    while True:
        if flag == 1:
            break
        for i in range(1,6): # 감소할 i
            a = password_lst.pop(0)
            password_lst.append((a)-i)
            if password_lst[-1] <= 0:
                password_lst[-1] = 0
                flag = 1
                break

    print(f'#{tc}', end = ' ')
    print(*password_lst)