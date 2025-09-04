# 주사위 3개를 던져서 합이 10 이하인 케이스 수

path = []
result = 0

def recur(cnt):
    global result
    
    # 이미 10을 넘은 경우는 더 볼 필요가 없다
    if sum(path) > 10:
        return
    
    if cnt == 3:
        if sum(path) <= 10:
            print(*path)
            result += 1
        return
    
    for num in range(1, 7):
        path.append(num)
        recur(cnt + 1)
        path.pop()


recur(0)


# 누적합을 활용하는 버전 <----------- 추천
def recur(cnt, total):
    global result
    
    # 이미 10을 넘은 경우는 더 볼 필요가 없다
    if total > 10:
        return
    
    if cnt == 3:
        if total <= 10:
            result += 1
        return
    
    for num in range(1, 7):
        recur(cnt + 1, total + num)

recur(0, 0)