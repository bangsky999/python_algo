# 순열
# [1,2,3,4,5,6,7] 3개의 카드가 존재  -> 2개를 뽑는다.

path = [] # 뽑은 카드들을 저장
used = [False] * 7 # 1 ~ 6까지의 카드 숫자 사용여부를 기록(0은 버린다) 
def recur(cnt):
    if cnt == 3:
        print(*path)
        return
    
    # 중복을 제거하기 위한 과정
    for num in range(1,7):
        if used[num]:
            continue


        # 넣었다가 초기화
        used[num] = 1
        path.append(num)
        recur(cnt+1)
        path.pop()
        used[num] = 0
recur(0)