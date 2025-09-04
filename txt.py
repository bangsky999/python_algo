# 주사위 누적합을 이용하는 버전
res = []
result = 0

def f(cnt, total):
    global result

    if total > 10:
        return
    
    if cnt == 3:
        if total <= 10:
            result += 1
            print(res)
        return

    for num in range(1, 7):
        res.append(num)
        f(cnt + 1, total + num)
        res.pop()


f(0, 0)