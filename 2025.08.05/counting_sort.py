def counting_sort(DATA, TEMP, k):
    '''
    DATA[] -- 입력 배열(원소는 0이상 k이하 정수)
    TEMP[] -- 정렬된 배열
    COUNTS[] -- 카운트 배열

    1. 발생 횟수 구하기
    2. 누적합 구하기
    3. 누적합을 줄이면서, TEMP에 저장

    ### 궁금한 점 ###
    
    '''
    # 아래에 값을 입력하시오.
    COUNTS = [0]*(k+1)

    for i in range(len(DATA)):
        COUNTS[DATA[i]] += 1

    for i in range(1, k+1):
        COUNTS[i] += COUNTS[i-1]

    for i in range(len(DATA)-1, -1, -1):
        COUNTS[DATA[i]] -= 1
        TEMP[COUNTS[DATA[i]]] = DATA[i]
    return TEMP





DATA = [0,4,1,3,1,2,4,1]
TEMP = [0] * len(DATA)
k = 4 # DATA 내 최댓값
print(counting_sort(DATA, TEMP, k))