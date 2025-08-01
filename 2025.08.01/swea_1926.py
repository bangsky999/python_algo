N = int(input())
# N개 만큼의 리스트 형성
lst = list(range(1, N+1))
# lst의 i번쨰를 가져와서
for i in lst:
    cnt = 0 # 3,6,9가 str(i)에 몇개 있는지
    for j in str(i):
        if j == '3':
            cnt += 1
        elif j == '6':
            cnt += 1
        elif j == '9':
            cnt += 1
    # 3,6,9가 있다면,,
    if cnt > 0:
        # 리스트를 숫자대신 '-'로 대체
        lst[i-1]='-'*cnt
for k in lst:
    print(k, end = ' ')