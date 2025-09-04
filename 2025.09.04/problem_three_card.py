# 카드 5장을 뽑았을 때, 
# 같은 종류의 카드가 3개 연속으로 나오는 경우의 수 - 카드는 A, J, Q, K

cards = ['A', 'J', 'Q', 'K']
path = []
result = 0

# 연속된 3개가 나오면 return true, 아니면 false
def count_three():
    if path[0] == path[1] == path[2]:
        return True
    if path[1] == path[2] == path[3]:
        return True
    if path[2] == path[3] == path[4]:
        return True
    return False # flag 초기화


def recur(cnt):
    global result
    if cnt == 5:
        # Todo: 연속된 3개가 나오면 counting
        if count_three(): # true가 된다면
            result += 1
            print(*path)
        return
    
    # 카드 중 하나를 선택
    for idx in range(len(cards)):
        path.append(cards[idx])
        recur(cnt + 1)
        path.pop()


recur(0)