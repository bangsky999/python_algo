# # 3명의 친구 부분집합 찾기
# arr = ['O', 'X']
# name = ['MIN', 'CO', 'TIM']
# path = []

# def recur(cnt):
#     # 종료조건
#     if cnt == 3:
#         print(*path)
#         return
    
#     # 재귀호출 파트
#     # - 부분집합에 포함되는 경우
#     path.append(arr[0])
#     recur(cnt+1)
#     path.pop()
#     # - 포함되지 않는 경우
#     path.append(arr[1])
#     recur(cnt+1)
#     path.pop()


# recur(0)


name = ['MIN', 'CO', 'TIM']


def recur(cnt, path):
    if cnt == 3:
        print(*path)
        return
    
    # 부분집합에 포함시키는 경우
    recur(cnt+1, path + [name[cnt]])
    # 포함시키지 않는 경우
    recur(cnt+1, path)

recur(0, [])