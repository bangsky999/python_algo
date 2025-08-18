### 영준이와 친구들 ? ###

N, M, L = map(int, input().split())
arr = [1]+[0]*(N-1)
cnt = 0 # 공을 던진 횟수
val = 0 # while문 플래그

i = 0 # 초기 인덱스
while val == 0:
    if val == 0:
        for arr_check in range(len(arr)):
            if arr[arr_check] == M:
                print(cnt)
                val = 1
                break
    if val == 1:
        break

    if arr[i] % 2 == 0: # 짝수라면
        if i-L < -N:
            i = i - L + N
            arr[i] += 1
            cnt += 1
        else:
            i -= L
            arr[i] += 1
            cnt += 1
    else: # 홀수라면
        if i+L <N: # 내부에 있으면
            i += L
            arr[i] += 1
            cnt += 1
        else: # 리스트 범위를 초과한다면
            i = i + L - N
            arr[i] += 1
            cnt += 1
    