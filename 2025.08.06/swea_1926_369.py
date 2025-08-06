### 369369 ### 
# 방법1
N = int(input())
arr = list(range(1, N+1))
# arr의 한 요소씩 꺼내기
for i in arr:
    # cnt는 요소에 들어있는 3,6,9를 세는 용도
    cnt = 0
    # 문자열로 i를 바꿔서 한단어씩 꺼내오고, 3,6,9 들어있으면 cnt += 1
    for j in str(i):
        if int(j) ==3:
            cnt += 1
        if int(j) ==6:
            cnt += 1
        if int(j) ==9:
            cnt += 1
        else:
            pass
    # 검사가 끝나고 cnt가 있으면 '-'*cnt 해주기
    if cnt != 0:
        arr[i-1] = '-'*cnt
    # 그렇지 않다면 문자열로 리스트에 반환
    else:
        arr[i-1] = str(i)

print(' '.join(map(str, arr)))

# 방법2
N = int(input())
arr = list(range(1, N+1))
for i in range(len(arr)):
    cnt = 0
    for j in str(arr[i]):
        if int(j) == 3:
            cnt += 1
        if int(j) == 6:
            cnt += 1
        if int(j) == 9:
            cnt += 1
        else:
            pass
    if cnt != 0:
        arr[i] = '-'*cnt
    else:
        arr[i] = str(arr[i])
for i in arr:
    print(i, end = ' ')